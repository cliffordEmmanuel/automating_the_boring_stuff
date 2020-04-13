# create a dictionary to categorize all the file types
import os
from pathlib import Path


SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt','.docx', '.xlsx'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    """this function returns the category of the file based on it's extensions"""
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return 'MISC'

def organizeDirectory():
    """this functions puts files in the current directory into their specific directory based on their file type"""
    for item in os.scandir():
        # returns a list of all files in the current directory
        if item.is_dir(): # making sure categories are skipped
            continue
        filePath = Path(item) # this gets the path of each item
        filetype = filePath.suffix.lower() # this isolates the extension of each file
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)  # casts the directory to a file path
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

organizeDirectory()

    

        


