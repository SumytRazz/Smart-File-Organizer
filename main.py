from pathlib import Path

FILE_CATEGORIES = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos"
}

test_folder = Path("test_files")

for item in test_folder.iterdir():
    if item.is_file():
        extension = item.suffix
        category = FILE_CATEGORIES.get(extension)
        folder_path = test_folder / category
        folder_path.mkdir(exist_ok=True)
        print(f"Created folder: {folder_path}")