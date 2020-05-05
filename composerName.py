from mutagen.easyid3 import EasyID3 as easyid3
import re, artistName


def modifyComposer(tags, song_name):
    if 'composer' in tags.keys() and tags['composer'][0] != '':
        print("Composer: ", tags['composer'][0])
    else:
        print("Curr Composer: None")
        artistName.start(tags, song_name, 0)
        tags['composer'] = tags['artist'][0]
        tags.save()
        print("New Composer: ", tags['composer'][0])


def start(tags, song_name):
    modifyComposer(tags, song_name)
