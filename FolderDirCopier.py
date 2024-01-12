"""
This script will take all the folder names and structure starting from a 
user defined input and copy them to another directory defined by the user
Created by Taylor Harrison
"""
import os
from IsFilePathValid import is_pathname_valid


def getFolders(startingDir:str)->list[str]:
    # Create empty list for all the folder directories
    directoryList: list[str] = []
    # Starting from the top, walk down and get the folder directory names
    for root, dirs, file in os.walk(startingDir, topdown=True):
        for name in dirs:
            startingIndex = len(startingDirectory)
            path = root + "\\" + name
            directoryList.append(path[startingIndex:])
    return directoryList

def createFolders(parentDir: str, folderNames: list[str]):
    for name in folderNames:
        # For each element in the folderNames list, iterate through and use
        # os.mkdir() create each folder at the desired path
        try: 
            os.mkdir(parentDir+name) 
            print(f"Directory {parentDir+name} created")
        except FileExistsError as error:
            # If the file exists, raise execption and do not make the directory
            print(f"Directory {parentDir+name} already exists. Directory not created")


if __name__ == "__main__":
    startingDirectory: str = input("Enter the starting folder directory you would like to emulate: ")
    newDirectory: str = input("Enter the starting folder directory you would like to create the new folders: ")
    if is_pathname_valid(startingDirectory) and is_pathname_valid(newDirectory) and os.path.exists(newDirectory) and os.path.exists(startingDirectory):
        folders = getFolders(startingDirectory)
        createFolders(newDirectory, folders)
    else:
        print("One of the file paths specified does not exist and/or is not valid, exiting program.")