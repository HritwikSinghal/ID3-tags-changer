from tools import *


def joinPathAndRename(oldNameWithPath, newName, full_path_of_songs):
    i = full_path_of_songs.index(oldNameWithPath)
    newNameWithPath = os.path.join(os.getcwd(), newName)
    full_path_of_songs[i] = newNameWithPath
    os.rename(oldNameWithPath, newNameWithPath)


def fixName(full_path_of_songs, songNameWithPath):
    oldName = re.findall(r'[^\\]+\.mp3', songNameWithPath)
    print("Current Name: ", oldName[0])

    newName = removeBitrate(oldName[0])
    newName = removeNonUtf8(newName)
    newName = removeSiteName(newName)
    if oldName[0] != newName:
        print("New Name    : ", newName)
        joinPathAndRename(songNameWithPath, newName, full_path_of_songs)


def start(songDir, full_path_of_songs, songNameWithPath):
    changeDir(songDir)
    fixName(full_path_of_songs, songNameWithPath)
