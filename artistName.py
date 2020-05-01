import re


def filterIndArtist(tags):
    currArtist = tags['artist']
    print("Curr Artist: ", currArtist[0])

    currArtist[0] = re.sub(r' &\w+|/\s*|,\s*', ';', currArtist[0])
    currArtist[0] = re.sub(r';\s*;\s*|;\s*', '; ', currArtist[0])

    # old one
    # currArtist[0] = ';'.join(re.split(r'/|,|& ', currArtist[0]))

    if currArtist[0] != tags['artist'][0]:
        tags['artist'] = currArtist[0]
        tags.save()
        print("New Artist: ", tags['artist'][0])


def start(tags):
    filterIndArtist(tags)
