def has_any_files(path):
    for _, _, files in os.walk(path):
        if files:
            return True
    return False
import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer import organize_file, KNOWN_FOLDERS
import stat # 🔹 New import to fix permissions

def remove_readonly(func, path, excinfo):
    """Clear the readonly bit and retry the deletion."""
    os.chmod(path, stat.S_IWRITE)
    func(path)
class ScannerHandler(FileSystemEventHandler):
    def __init__(self, base_dir, log_func):
        self.base_dir = base_dir
        self.log_func = log_func
    
    def initial_scan(self):
        for item in os.listdir(self.base_dir):
            full_path = os.path.join(self.base_dir, item)

            if item in KNOWN_FOLDERS or item == "Others":
                continue

            if os.path.isdir(full_path):
                self.process_directory(full_path)

    def process_directory(self, dir_path):
    # Take snapshot of all files FIRST
        files_snapshot = []
        for root, _, files in os.walk(dir_path):
            for f in files:
                files_snapshot.append(os.path.join(root, f))

        

        # Move all files
        for file_path in files_snapshot:
            if os.path.exists(file_path):
                result = organize_file(file_path, self.base_dir)
                self.log_func(result)

        # 🔥 FORCE DELETE THE FOLDER AFTER MOVING FILES
        time.sleep(1)

        try:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path, onerror=remove_readonly)
                self.log_func(f"Deleted folder: {os.path.basename(dir_path)}")
                self.cleanup_parent_if_empty(dir_path)
        except Exception as e:
            self.log_func(f"Folder delete failed: {e}")

    def cleanup_parent_if_empty(self, path):
        parent = os.path.dirname(path)
        if parent == self.base_dir:
            return
        try:
            if os.path.exists(parent) and not os.listdir(parent):
                shutil.rmtree(parent, onerror=remove_readonly)
                self.log_func(f"Cleaned parent folder: {os.path.basename(parent)}")
                self.cleanup_parent_if_empty(parent)
        except Exception as e:
            self.log_func(f"Parent cleanup skipped: {e}")

    def on_created(self, event):
        rel_path = os.path.relpath(event.src_path, self.base_dir)
        first_dir = rel_path.split(os.sep)[0]
        if first_dir in KNOWN_FOLDERS or first_dir == "Others":
            return

        if event.is_directory:
            # 🔴 DO NOTHING for folders
            return

        # ✅ HANDLE FILES ONLY
        result = organize_file(event.src_path, self.base_dir)
        self.log_func(result)

        # After moving a file, try cleaning its parent folder
        parent = os.path.dirname(event.src_path)
        time.sleep(1)
        self.process_directory(parent)


def start_scanner(path, log_func):
    handler = ScannerHandler(path, log_func)

    # initial cleanup for already existing folders
    handler.initial_scan()

    observer = Observer()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    return observer

