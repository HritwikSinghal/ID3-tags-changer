from mutagen.easyid3 import EasyID3 as easyid3
import re
from listPrint import print_list


def append_artists(full_path_of_songs):
    for song in full_path_of_songs:
        audio = easyid3(song)
        currArtist = audio['artist']

        print("Song title: ", audio['title'][0])
        print("Curr Artist: ", currArtist[0])
        currArtist[0] = ';'.join(re.split(r'/|,|&', currArtist[0]))
        if currArtist[0] != audio['artist'][0]:
            audio['artist'] = currArtist[0]
            audio.save()
            print("New Artist: ", audio['artist'][0])
        else:
            print("No change, Artist is already formatted correctly.")
        print()


def start(full_path_of_songs):
    print("-------------Changing Artists....-------------")
    append_artists(full_path_of_songs)
    print("-------------Changing Artists Done.-------------")
