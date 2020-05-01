import os
import re


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
    # and removes everything after djmaza including
    # .mp3 extension. So re-add it.

    x = re.compile(r'''
    (
    \s*-*\s*                                # for foo - bar
    \[*                                     # for foo [bar or foo [bar]
    w*\.*                                   # for www.foobar
    (d|D)(j|J)(m|M)aza
    .*                                   # for foobar.XXX XXX XXX
    )
    ''', re.VERBOSE)

    newName = x.sub('', oldName)
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
