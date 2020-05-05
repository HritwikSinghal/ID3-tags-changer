import os
import re

import retrieveTags


# -----------------------------------------------------#
# Website Name Specifics

def removeDjX(oldName):
    # for DJMXXX

    x = re.compile(r'''
    (
    \s*-*\s*                                # for foo - bar
    \[*                                     # for foo [bar or foo [bar]
    w*\.*                                   # for www.foobar
    [dD][jJ][mM]aza
    .*                                   # for foobar.XXX XXX XXX
    )
    ''', re.VERBOSE)

    newName = x.sub('', oldName)
    return newName


def removeSonX(oldName):
    # for SongsXX

    x = re.compile(r'''
    (
    \s*-*\s*                                # for foo - bar
    \[*                                     # for foo[bar or foo[bar]
    w*\.*                                   # for www.foobar
    [sS]ongs
    .*                                   # for foobar.XXX XXX XXX
    )
    ''', re.VERBOSE)

    newName = x.sub('', oldName)
    return newName


def removeMPXX(oldName):
    # for MPXX

    x = re.compile(r'''
    (
    \s*-*\s*                                # for foo - bar
    \[*                                     # for foo[bar or foo[bar]
    w*\.*                                   # for www.foobar
    [mM][pP]3[kK]
    .*                                   # for foobar.XXX XXX XXX
    )
    ''', re.VERBOSE)

    newName = x.sub('', oldName)
    return newName


def removeSiteName(oldName):
    # supportes SonXXX, DjXXX, MPXX as of now
    # and removes everything after site name
    # including .mp3 extension. So re-add it.

    newName = removeDjX(oldName)
    newName = removeSonX(newName)
    newName = removeMPXX(newName)
    return newName


# ----------------------------------------------#


def removeBitrate(oldName):
    # old method
    # x = re.compile(r'\s*\[*(\d+(.*kbps|Kbps|KBPS|KBps))\]*')

    x = re.compile(r'''
    \s*-*\s*                            # for foo - bar
    \[*                                 # for foo [bar
    \d*\s*[kK][bB][pP][sS]         # for KBps or KBPS or kbps or Kbps
    \]*                                 # for foo bar]
    ''', re.VERBOSE)

    newName = x.sub('', oldName)
    return newName


def removeYear(oldName):
    # it removes any number in
    # string within () and brackets itself

    newName = re.sub(r' \(\d*\)', '', oldName)
    return newName


def removeGibberish(oldName):
    newName = re.sub(r'&quot;|&*amp', '', oldName)
    return newName


def removeTrailingExtras(oldName):
    # newName = re.sub(r'&quot;|&*amp', '', oldName)
    newName = re.sub(r';\s*;\s*', '; ', oldName)
    return newName


def divideBySColon(oldName):
    namesDivided = re.sub(r'\s*[&/,]\s*', ';', oldName)
    return namesDivided


def removeDup(old_name):
    new_name = old_name.split(';')
    new_name = map(str.strip, new_name)

    new_name = list(set(new_name))
    new_name = ';'.join(new_name)

    return new_name


# ------------------------------------------#
# Extras

def getSongNameWithoutPath(songNameWithPath):
    songNameWithoutPath = re.findall(r'[^\\]+\.mp3', songNameWithPath)
    return songNameWithoutPath[0]


def printList(myList):
    print('--------------')
    for item in myList:
        print(item)
    print('--------------\n')


def printDict(myDict):
    print('-----------')
    for key, value in myDict.items():
        print(key, ':', value)
    print('-----------')


def changeDir(songDir):
    os.chdir(songDir)


def fixImageUrl(oldUrl):
    url = oldUrl.replace('150x150', '500x500')
    return url


# ---------------------------------------------#


def isTagPresent(song_tags, tag_name):
    if tag_name in song_tags.keys() and song_tags[tag_name] != '':
        return True
    return False


def addIfTagMissing(tags, tag_name, song_name):
    if not isTagPresent(tags, tag_name):
        retrieveTags.start(tags, song_name, tag_name)
