import os


def isImageFile(filename):
    if (
        filename.endswith(".jpg")
        or filename.endswith(".jpeg")
        or filename.endswith(".png")
    ):
        return True
    return False


def trainingFolderValid(dirpath):
    for filename in os.listdir(dirpath):
        if not isImageFile(filename):
            return False
    return True
