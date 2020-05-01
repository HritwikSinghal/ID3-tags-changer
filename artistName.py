from mutagen.easyid3 import EasyID3 as easyid3
import re
from listPrint import print_list


def modifyArtist(audio, currArtist):
    currArtist[0] = re.sub(r' &\w+|/\s*|,\s*', ';', currArtist[0])
    currArtist[0] = re.sub(r';\s*;\s*|;\s*', '; ', currArtist[0])

    # old one
    # currArtist[0] = ';'.join(re.split(r'/|,|& ', currArtist[0]))

    if currArtist[0] != audio['artist'][0]:
        audio['artist'] = currArtist[0]
        audio.save()
        print("New Artist: ", audio['artist'][0])
    else:
        print("No change, Artist is already formatted correctly.")
    print()


def changeArtist(full_path_of_songs):
    for song in full_path_of_songs:
        audio = easyid3(song)
        currArtist = audio['artist']
        print("Song title: ", audio['title'][0])
        print("Curr Artist: ", currArtist[0])
        modifyArtist(audio, currArtist)


def start(full_path_of_songs):
    print("-------------Changing Artists....-------------")
    changeArtist(full_path_of_songs)
    print("-------------Changing Artists Done.-------------")
