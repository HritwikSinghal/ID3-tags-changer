import os, re, traceback
from listPrint import print_list


def changeDir(songDir):
    os.chdir(songDir)


def removeBitrate(oldName):
    # old method
    # x = re.compile(r'\s*\[*(\d+(.*kbps|Kbps|KBPS|KBps))\]*')

    x = re.compile(r'''
    \s*-*\s*                            # for foo - bar
    \[*                                 # for foo [bar
    (\d+(.*kbps|Kbps|KBPS|KBps))        # for KBps or KBPS or kbps or Kbps
    \]*                                 # for foo bar]
    ''', re.VERBOSE)

    newName = x.sub('', oldName)
    return newName


def removeNonUtf8(oldName):
    newName = re.sub(r'&quot;', '', oldName)
    return newName


def removeSiteName(oldName):
    # only supported DJMXXX as of now
    # newName = re.sub(r'', '', newName)
    x = re.compile(r'''
    (
    \s*-*\s*                                # for foo - bar
    \[*                                     # for foo [bar or foo [bar]
    (d|D)(j|J)(m|M)aza
    \.*
    [^.mp3]*                                # stop at .mp3
    )
    ''', re.VERBOSE)

    # print(x.findall(oldName))
    newName = x.sub('', oldName)
    # print(newName)
    return newName


def removeTrailingExtras():
    pass


def pathJoinRename(name):
    pass
    # if newActualName[0] != oldName[0]:
    #     os.rename(songNameWithPath, newName)
    #     print("New Name    : ", newActualName[0])
    #     full_path_of_songs[i] = newName
    # old
    # method
    # newName = re.findall(r'(.+) \[.*\](.mp3)', songNameWithPath)


def filterName(full_path_of_songs):
    print("-------------Filtering song name...-------------")

    for songNameWithPath in full_path_of_songs:
        oldName = re.findall(r'[^\\]+\.mp3', songNameWithPath)
        # print("Current Name: ", oldName[0])
        print(oldName[0])

        newName = removeBitrate(oldName[0])
        newName = removeNonUtf8(newName)
        newName = removeSiteName(newName)

        print(newName)
        print()

    print("-------------Filtering song name Done.-------------")
    return full_path_of_songs


def start(full_path_of_songs, songDir):
    changeDir(songDir)
    full_path_of_songs = filterName(full_path_of_songs)
