# Created On 16/11/2024
import os
import time
import shutil
from pathlib import Path
import logging


#Defining The Several Files Format
file_types = {
    'image': [".png", ".jpg", ".jpeg", ".raw", ".bmp", ".gif", ".tiff"], # Images Format
    'document': [".docx", ".doc", ".ppt", ".pdf", ".pptx", ".txt", ".xls", ".xlsx"],# Documents Format
    'compressed': [".zip", ".7z", ".rar", ".iso", ".tar", ".gz"],# Compressed Format
    'audio': [".mp3", ".wav", ".ogg", ".aac", ".flac"],# Audios Format
    'video': [".mp4", ".av1", ".avi", ".mov", ".mkv"] # Videos Format
}

logging.basicConfig(
    filename='logs.txt', # Logs File Name
    level=logging.DEBUG, # Logs Level
    format='%(asctime)s    -   %(levelname)s    - %(message)s' # Logs Message Format
)

# Main Function For Organising Files
def FileOrganiser(directory):
    # Converting directory to path object
    directory = Path(directory)
    # Check the Validity of the directory
    if not directory.is_dir():
        print("Directory Path Is Invalid !")
        return
    print(f"Directory Found: '{directory.name}'")

    # Scan all files in the directory
    files = [file for file in directory.iterdir() if file.is_file()]

    # Get Files Extensions
    for file in files:
        file_extension = file.suffix.lower()
        dest_folder = None

        # Attach to each file the suitable folder
        for folder,extension in file_types.items():
            if file_extension in extension:
                dest_folder = folder
                break

        # Execeptions to unknown or undefined files formats
        if not dest_folder:
            dest_folder = 'Others'

        # Create Destination Folder
        subfolder = directory / dest_folder
        subfolder.mkdir(exist_ok=True)

        # Handle Duplicated Files
        new_file_path = subfolder / file.name
        counter = 1
        while new_file_path.exists():
            new_file_path = subfolder / f"{file.stem}{counter}{file.suffix}"
            counter += 1
        # Moving Files to Their folders
        try:
            shutil.move(file, new_file_path)
            logging.info(f"File {file.name} Moved To {new_file_path}")
        except Exception as e:
            logging.error(f"Cannot Move {file.name}")

# Auto run the Function When The .py File executed
if __name__ == "__main__":
    directory = input("Enter The Directory path: ")
    FileOrganiser(directory)