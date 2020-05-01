from mutagen.easyid3 import EasyID3 as easyid3
import re, artistName
from listPrint import print_list


def append_composer(full_path_of_songs):
    for song in full_path_of_songs:
        audio = easyid3(song)
        print("Song title: ", audio['title'][0])

        if 'composer' in audio.keys():
            print("Curr Composer: ", audio['composer'][0])
        else:
            print("Curr Composer: None")
        artistName.modifyArtist(audio, full_path_of_songs)
        audio['composer'] = audio['artist'][0]
        audio.save()
        print("New Composer: ", audio['composer'][0])
        print()


def start(full_path_of_songs):
    print("-------------Changing Composers...-------------")
    append_composer(full_path_of_songs)
    print("-------------Changing Composers Done.-------------")
