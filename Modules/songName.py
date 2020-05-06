from Base.tools import *
from Base.tools import getSongNameWithoutPath


def joinPathAndRename(oldNameWithPath, newName, full_path_of_songs):
    i = full_path_of_songs.index(oldNameWithPath)

    newNameWithPath = os.path.join(os.getcwd(), newName)
    full_path_of_songs[i] = newNameWithPath
    try:
        os.rename(oldNameWithPath, newNameWithPath)
    except FileExistsError:
        print("File with name '" + newName + "' already exists")
        x = int(input("do you want to delete that file?"
                      "\n1 == Yes,\n"
                      "0 == NO\n"))
        if x == 1:
            os.remove(newNameWithPath)
            print("File removed successfully. Now renaming new file.")
            os.rename(oldNameWithPath, newNameWithPath)
            print("File renamed successfully.")
        else:
            print("Moving on to next file...")


def fixName(full_path_of_songs, songNameWithPath):
    oldName = getSongNameWithoutPath(songNameWithPath)
    print("Current Name: ", oldName)

    newName = removeBitrate(oldName)
    newName = removeGibberish(newName)
    newName = removeSiteName(newName)
    newName = (newName.replace('.mp3', '')).strip()

    if '.mp3' not in newName:
        newName = newName + '.mp3'

    if oldName != newName:
        print("New Name    : ", newName)
        joinPathAndRename(songNameWithPath, newName, full_path_of_songs)


def start(songDir, full_path_of_songs, songNameWithPath):
    changeDir(songDir)
    fixName(full_path_of_songs, songNameWithPath)
