from mutagen.easyid3 import EasyID3 as easyid3
import re


def removeYearAndExtraCharIfExist(tags):
    albumName = tags['album'][0]
    newName = re.sub(r' \(\d*\)|&quot;', '', albumName)
    if newName != albumName:
        tags['album'] = newName


def modifyAlbum(tags):
    print("Curr Album Name: ", tags['album'][0])

    removeYearAndExtraCharIfExist(tags)
    oldAlbumName = tags['album'][0]

    newAlbumName = tags['album'][0] + ' (' + tags['date'][0] + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", newAlbumName)


def start(tags):
    modifyAlbum(tags)
