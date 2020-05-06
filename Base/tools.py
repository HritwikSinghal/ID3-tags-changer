import os
import re
import platform


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
    new_name.sort()
    new_name = ';'.join(new_name)

    return new_name


# ------------------------------------------#
# Extras

# def getSongNameWithoutPath(songNameWithPath):
#     if platform.system() == 'Windows':
#         # Dont know why '[^\\]+\.mp3' works.
#         songNameWithoutPath = re.findall(r'[^\\]+\.mp3', songNameWithPath)
#     else:
#         songNameWithoutPath = re.findall(r'[^/]+\.mp3', songNameWithPath)
#     return songNameWithoutPath[0]

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


def join(a, b):
    return os.path.join(a, b)


# ---------------------------------------------#


def isTagPresent(tags, tag_name):
    if tag_name in tags.keys() and tags[tag_name] != '':
        return True
    return False


def saveTags(tag_name, tag_value_from_json, tags):
    tags[tag_name] = tag_value_from_json
    tags.save()
    print("Added " + tag_name)


def checkAndFixTag(tags, tag_name, tag_value_from_json, ask_flag=1):
    if not isTagPresent(tags, tag_name):
        saveTags(tag_name, tag_value_from_json, tags)
    elif tag_value_from_json != tags[tag_name]:
        if ask_flag == 1:
            print("{} retrieved and current {} do not match, Select the one "
                  "you want to keep. \nFirst one is retrieved from web, "
                  "2nd is current one".format(tag_name, tag_name))
            print("1) {}\n2) {}".format(tag_value_from_json, tags[tag_name][0]))

            x = int(input())
            if x == 1:
                saveTags(tag_name, tag_value_from_json, tags)
            else:
                print("No change")
        else:
            saveTags(tag_name, tag_value_from_json, tags)
