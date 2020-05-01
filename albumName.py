from mutagen.easyid3 import EasyID3 as easyid3
import re
from listPrint import print_list


def removeYearAndExtraCharIfExist(full_path_of_songs):
    print("--Removing Year If Exists in Album Name ....--")

    for song in full_path_of_songs:
        tags = easyid3(song)
        albumName = tags['album'][0]
        print("Curr Name: ", albumName)

        # old method
        # newName = re.findall(r'(.*) \(\d+\)', albumName)
        newName = re.sub(r' \(\d*\)|&quot;', '', albumName)
        if newName != albumName:
            print("New Name : ", newName)
            tags['album'] = newName
            tags.save()

    print("--Removing Year Done--")


def renameAlbum(full_path_of_songs):
    removeYearAndExtraCharIfExist(full_path_of_songs)

    # rename album name
    for song in full_path_of_songs:
        tags = easyid3(song)
        tags['album'] = (tags['album'][0] +
                         ' (' + tags['date'][0] + ')')

        tags.save()
        print("New Name : ", tags['album'][0])


def start(full_path_of_songs):
    print("-------------Renaming album names....-------------")
    renameAlbum(full_path_of_songs)
    print("-------------Renaming album names Done.-------------")
