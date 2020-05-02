from mutagen.easyid3 import EasyID3 as easyid3
import re
from tools import *


def modifyTitle(tags):
    print("Curr Title: ", tags['title'][0])

    oldTitle = tags['title'][0]
    newTitle = removeSiteName(oldTitle)
    newTitle = removeNonUtf8(newTitle)

    if oldTitle != newTitle:
        tags['title'] = newTitle
        tags.save()
        print("New Title : ", newTitle)


def start(tags):
    modifyTitle(tags)

