from Base.tools import *
from Base.tools import join


def joinPathAndRename(old_name, newName, songDir, song_list):
    # get index of current song from list
    index = song_list.index(old_name)

    newNameWithPath = join(songDir, newName)
    song_list[index] = newName

    try:
        os.rename(join(songDir, old_name), newNameWithPath)
    except FileExistsError:
        print("File with name '" + newName + "' already exists")
        x = int(input("Do you want to PERMANENTLY delete this old file?"
                      "\n1 == Yes, 0 == NO\n"))
        if x == 1:
            os.remove(newNameWithPath)
            print("File removed successfully. Now renaming new file.")

            os.rename(join(songDir, old_name), newNameWithPath)
            print("File renamed successfully.")

            del song_list[index]
        else:
            print("Moving on to next file...")


def fixName(songDir, old_name, song_list):
    print("Current Name: ", old_name)

    newName = removeBitrate(old_name)
    newName = removeGibberish(newName)
    newName = removeSiteName(newName)
    newName = (newName.replace('.mp3', '')).strip()

    if '.mp3' not in newName:
        newName = newName + '.mp3'

    if old_name != newName:
        print("New Name    : ", newName)
        joinPathAndRename(old_name, newName, songDir, song_list)


def start(songDir, song, song_list):
    changeDir(songDir)
    fixName(songDir, song, song_list)
