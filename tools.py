import os
import re


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


def removeTrailingExtras(oldName):
    pass


def removeYear(oldName):
    newName = re.sub(r' \(\d*\)', '', oldName)
    return newName


def print_list(my):
    print('--------------')
    for _ in my:
        print(_)
    print('--------------\n')


def changeDir(songDir):
    os.chdir(songDir)
