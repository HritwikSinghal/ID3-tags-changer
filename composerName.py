from mutagen.easyid3 import EasyID3 as easyid3
import re
from listPrint import print_list


def append_composer(full_path_of_songs):
    for song in full_path_of_songs:
        audio = easyid3(song)
        currArtist = audio['artist']
        currArtist[0] = ';'.join(re.split(r'/|,|&', currArtist[0]))
        audio['composer'] = currArtist[0]
        audio.save()


def start(full_path_of_songs):
    print("-------------Changing Composers...-------------")
    append_composer(full_path_of_songs)
    print("-------------Changing Composers Done.-------------")

