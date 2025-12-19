import os
import shutil
import time
from ml_model import predict_folder

KNOWN_FOLDERS = {
    "Documents",
    "Music",
    "Images",
    "Code",
    "Shortcuts",
    "Executables"
}

def wait_until_ready(file_path, retries=5, delay=0.5):
    last_size = -1
    for _ in range(retries):
        if not os.path.exists(file_path):
            return False

        size = os.path.getsize(file_path)
        if size == last_size:
            return True

        last_size = size
        time.sleep(delay)

    return False


def organize_file(file_path, base_dir):
    filename = os.path.basename(file_path)

    if not wait_until_ready(file_path):
        return f"Skipped (busy): {filename}"

    try:
        folder = predict_folder(filename)
    except Exception:
        folder = "Others"

    # 🔹 If ML predicts something unknown → Others
    if folder not in KNOWN_FOLDERS:
        folder = "Others"

    target_dir = os.path.join(base_dir, folder)
    os.makedirs(target_dir, exist_ok=True)

    # Inside organizer.py
    try:
        shutil.move(file_path, os.path.join(target_dir, filename))
        return f"{filename} → {folder}"
    except Exception as e:
        return f"Error moving {filename}: {e}"


# In organizer.py
def initial_scan(base_dir, log_func):
    # topdown=False ensures we empty the subfolders before deleting them
    for root, dirs, files in os.walk(base_dir, topdown=False):
        # Skip folders we already organized
        dirs[:] = [d for d in dirs if d not in KNOWN_FOLDERS and d != "Others"]
        
        for item in files:
            full_path = os.path.join(root, item)
            result = organize_file(full_path, base_dir)
            log_func(result)

        # Cleanup empty folders
        if root != base_dir:
            try:
                if not os.listdir(root):
                    os.rmdir(root)
                    log_func(f"Removed empty: {os.path.basename(root)}")
            except:
                pass