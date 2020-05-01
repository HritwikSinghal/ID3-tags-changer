from mutagen.easyid3 import EasyID3 as easyid3
import re, artistName
from listPrint import print_list


def modifyComposer(tags):
    if 'composer' in tags.keys() and tags['composer'][0] != '':
        print("Composer: ", tags['composer'][0])
    else:
        print("Curr Composer: None")
        artistName.filterIndArtist(tags)
        tags['composer'] = tags['artist'][0]
        tags.save()
        print("New Composer: ", tags['composer'][0])


def start(tags):
    modifyComposer(tags)
