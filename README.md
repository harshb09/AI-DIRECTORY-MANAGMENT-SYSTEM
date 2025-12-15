# AI-DIRECTORY-MANAGMENT-SYSTEM
import os
import shutil

FOLDER_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".py", ".cpp", ".c", ".java", ".js", ".html", ".css"]
}

def organize_directory(path):
    if not os.path.exists(path):
        print("Invalid path")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            moved = False
            for folder, extensions in FOLDER_MAP.items():
                if ext in extensions:
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(path, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, os.path.join(other_path, file))

    print("Directory organized successfully!")

if __name__ == "__main__":
    target_path = input("Enter directory path: ")
    organize_directory(target_path)
