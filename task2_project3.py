import os
from pathlib import Path

file_type = {
    "images": ['.png', '.jpeg', '.gif', '.psd', '.svg'],
    "audio": ['.aac', '.dvf', '.m4b', '.mp3', '.raw'],
    "video": ['.avi', '.flv', '.mov', '.qt', '.3gp'],
    "documents": ['.oxps', '.epub', '.pages', '.fdf', '.xsn']
}

# Map extension → folder
dct = {}
for directory, file_formats in file_type.items():
    for file_format in file_formats:
        dct[file_format] = directory

def file_organizer():
    for entry in os.scandir("."):
        if entry.is_dir():
            continue

        file_path = Path(entry.path)
        file_format = file_path.suffix.lower()

        if file_format in dct:
            directory_path = Path(dct[file_format])
        else:
            directory_path = Path("others")

        directory_path.mkdir(exist_ok=True)
        file_path.rename(directory_path / file_path.name)

if __name__ == "__main__":
    file_organizer()
