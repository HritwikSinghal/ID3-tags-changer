import os, re, traceback
from listPrint import print_list


def changeDir(songDir):
    os.chdir(songDir)


def filterName(full_path_of_songs):
    print("-------------Filtering song name...-------------")

    i = -1
    # remove 'XXX kbps' and '&quot;' from name
    for songName in full_path_of_songs:
        i += 1

        oldActualName = re.findall(r'[^\\]+\.mp3', songName)
        print("Current Name: ", oldActualName[0])

        # old method
        # newName = re.findall(r'(.+) \[.*\](.mp3)', songName)
        newName = re.sub(r' \[\d* .*\]| \d+kbps|&quot;', '', oldActualName[0])
        newActualName = re.findall(r'[^\\]+\.mp3', newName)

        if newActualName[0] != oldActualName[0]:
            os.rename(songName, newName)
            print("New name: ", newActualName[0])
            full_path_of_songs[i] = newName

    print("-------------Filtering song name Done.-------------")
    return full_path_of_songs


def start(full_path_of_songs, songDir):
    changeDir(songDir)
    full_path_of_songs = filterName(full_path_of_songs)
