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


def joinPathAndRename(oldNameWithPath, newName, full_path_of_songs):
    i = full_path_of_songs.index(oldNameWithPath)
    newNameWithPath = os.path.join(os.getcwd(), newName)
    full_path_of_songs[i] = newNameWithPath
    os.rename(oldNameWithPath, newNameWithPath)
    return full_path_of_songs


def fixName(full_path_of_songs):
    print("-------------Fixing song names...-------------")

    for songNameWithPath in full_path_of_songs:
        oldName = re.findall(r'[^\\]+\.mp3', songNameWithPath)
        print("Current Name: ", oldName[0])

        newName = removeBitrate(oldName[0])
        newName = removeNonUtf8(newName)
        newName = removeSiteName(newName)
        if oldName[0] != newName:
            print("New Name    : ", newName)
            full_path_of_songs = joinPathAndRename(songNameWithPath, newName, full_path_of_songs)

    print("-------------Fixing song names Done.-------------")
    return full_path_of_songs


def start(full_path_of_songs, songDir):
    changeDir(songDir)
    full_path_of_songs = fixName(full_path_of_songs)
