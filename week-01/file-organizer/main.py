from pathlib import Path
import shutil

folder = Path(".")

categories = {
    "Documents": [".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".xlsx",
        ".xls",
        ".ppt",
        ".pptx",
        ".csv"],
    "Images": [".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp"],
    "Videos": [ ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv"],
    "Music": [".mp3",
        ".wav",
        ".aac",
        ".flac",
        ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []
}

for category in categories:
    destination = folder / category
    destination.mkdir(exist_ok=True)

print("Folders created successfully!")

for item in folder.iterdir():
    if item.is_file():
        extension = item.suffix.lower()

        for category, extensions in categories.items():
            if extension in extensions:
                destination = folder / category / item.name
                shutil.move(item, destination)

                print(f"Moved: {item.name} → {category}")
                break