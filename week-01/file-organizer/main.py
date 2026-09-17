from pathlib import Path
import shutil

folder = Path(".")

categories = {
    "Documents": [".pdf",".doc",".docx",".txt",".xlsx",".xls",".ppt",".pptx",".csv"],
    "Images": [".jpg",".jpeg",".png",".gif",".bmp",".webp"],
    "Videos": [ ".mp4",".mkv",".avi",".mov",".wmv"],
    "Music": [".mp3",".wav",".aac",".flac",".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

def create_folders(folder, categories):
    for category in categories:
        destination = folder / category
        destination.mkdir(exist_ok=True)

def get_category(extension, categories):
    for category, extensions in categories.items():
        if category == "Others":
            continue
        if extension in extensions:
            return category
    return "Others"

def organize_files(folder, categories):
    moved_count = 0
    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix.lower()
            category = get_category(extension, categories)
            destination = folder / category / item.name
            try:
                shutil.move(item, destination)
                moved_count += 1
                print(f"Moved: {item.name} → {category}")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")
    print(f"Total files moved: {moved_count}")

def main():
    folder = Path(".")
    create_folders(folder, categories)
    organize_files(folder, categories)

if __name__ == "__main__":
    main()