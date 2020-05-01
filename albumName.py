from mutagen.easyid3 import EasyID3 as easyid3
import re


def removeYearAndExtraCharIfExist(tags):
    albumName = tags['album'][0]
    newName = re.sub(r' \(\d*\)|&quot;', '', albumName)
    if newName != albumName:
        tags['album'] = newName
        tags.save()


def modifyAlbum(tags):
    oldAlbumName = tags['album'][0]
    print("Curr Album Name: ", oldAlbumName)

    removeYearAndExtraCharIfExist(tags)

    newAlbumName = tags['album'][0] + ' (' + tags['date'][0] + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", tags['album'][0])


def start(tags):
    modifyAlbum(tags)
