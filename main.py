from pathlib import Path
import shutil

FILE_CATEGORIES = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".mp4": "Videos"
}


def get_category(extension):

    return FILE_CATEGORIES.get(extension, "Others")


test_folder = Path("test_files")

for item in test_folder.iterdir():

    if item.is_file():

        if item.name == "organizer.py":
            continue

        extension = item.suffix.lower()
        category = get_category(extension)
        folder_path = test_folder / category
        folder_path.mkdir(exist_ok=True)
        destination = folder_path / item.name
        shutil.move(item, destination)
        print(f"Moved: {item.name} -> {category}")