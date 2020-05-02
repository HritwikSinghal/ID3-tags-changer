from tools import *
from tools import getSongNameWithoutPath


def joinPathAndRename(oldNameWithPath, newName, full_path_of_songs):
    i = full_path_of_songs.index(oldNameWithPath)

    newNameWithPath = os.path.join(os.getcwd(), newName)
    full_path_of_songs[i] = newNameWithPath

    os.rename(oldNameWithPath, newNameWithPath)


def fixName(full_path_of_songs, songNameWithPath):
    oldName = getSongNameWithoutPath(songNameWithPath)
    print("Current Name: ", oldName)

    newName = removeBitrate(oldName)
    newName = removeGibberish(newName)
    newName = removeSiteName(newName)

    if '.mp3' not in newName:
        newName = newName + '.mp3'

    if oldName != newName:
        print("New Name    : ", newName)
        joinPathAndRename(songNameWithPath, newName, full_path_of_songs)


def start(songDir, full_path_of_songs, songNameWithPath):
    changeDir(songDir)
    fixName(full_path_of_songs, songNameWithPath)
