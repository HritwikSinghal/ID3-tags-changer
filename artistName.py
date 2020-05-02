import re
from tools import *


def filterIndArtist(tags):
    oldArtist = tags['artist'][0]
    print("Curr Artist: ", oldArtist)

    # old one
    # oldArtist = ';'.join(re.split(r'/|,|& ', oldArtist))

    # 2nd old method
    # oldArtist = re.sub(r'\s*&\s*|\s*/\s*|\s*,\s*', ';', oldArtist)
    # oldArtist = re.sub(r';\s*;\s*|;\s*', '; ', oldArtist)

    # new method
    newArtist = divideBySColon(oldArtist)

    if newArtist != oldArtist:
        tags['artist'] = newArtist
        tags.save()
        print("New Artist: ", newArtist)


def start(tags):
    filterIndArtist(tags)
