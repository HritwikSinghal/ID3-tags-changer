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

    newName = x.sub('', oldName)
    return newName


def removeTrailingExtras():
    pass


def removeYear(oldName):
    newName = re.sub(r' \(\d*\)', '', oldName)
    return newName
