from mutagen.easyid3 import EasyID3 as easyid3
import re
from listPrint import print_list


def append_artists(full_path_of_songs):
    for song in full_path_of_songs:
        audio = easyid3(song)
        currArtist = audio['artist']
        # print("Artist: ", currArtist[0])
        currArtist[0] = ';'.join(re.split(r'/|,|&', currArtist[0]))
        audio['artist'] = currArtist[0]
        audio.save()


def start(full_path_of_songs):
    append_artists(full_path_of_songs)
