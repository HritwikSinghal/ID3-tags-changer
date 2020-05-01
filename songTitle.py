from mutagen.easyid3 import EasyID3 as easyid3
import re
from tools import removeYear


def modifyTitle(tags):
    print("Curr Title: ", tags['title'][0])

    # oldAlbumName = tags['album'][0]
    #
    # newAlbumName = tags['album'][0] + ' (' + tags['date'][0] + ')'
    #
    # if oldAlbumName != newAlbumName:
    #     tags['album'] = newAlbumName
    #     tags.save()
    #     print("New Album Name : ", newAlbumName)


def start(tags):
    modifyTitle(tags)
