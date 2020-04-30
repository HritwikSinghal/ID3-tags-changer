from mutagen.easyid3 import EasyID3 as easyid3
import re
from listPrint import print_list


def removeYearIfExist(full_path_of_songs):
    for song in full_path_of_songs:
        tags = easyid3(song)
        albumTag = tags['album']

        x = re.findall(r'(.*) \(\d+\)', albumTag[0])
        if len(x) != 0:
            # print(tags['album'])
            tags['album'] = x[0]
            tags.save()


def changeAlbumName(full_path_of_songs):
    removeYearIfExist(full_path_of_songs)

    # rename album name
    for song in full_path_of_songs:
        tags = easyid3(song)
        tags['album'] = (tags['album'][0] +
                         ' (' + tags['date'][0] + ')')
        tags.save()


def start(full_path_of_songs):
    changeAlbumName(full_path_of_songs)
