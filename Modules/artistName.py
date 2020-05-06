from Base import tools


def filterIndArtist(tags, flag=1):
    oldArtist = tags['artist'][0]

    print("Curr Artist: ", oldArtist)

    # old one
    # oldArtist = ';'.join(re.split(r'/|,|& ', oldArtist))

    # 2nd old method
    # oldArtist = re.sub(r'\s*&\s*|\s*/\s*|\s*,\s*', ';', oldArtist)
    # oldArtist = re.sub(r';\s*;\s*|;\s*', '; ', oldArtist)

    # new method
    newArtist = tools.removeGibberish(oldArtist)
    newArtist = tools.divideBySColon(newArtist)

    newArtist = tools.removeTrailingExtras(newArtist)
    newArtist = tools.removeDup(newArtist)

    if newArtist != oldArtist:
        tags['artist'] = newArtist
        tags.save()
        print("New Artist: ", newArtist)


def start(tags, song_name, song_info):
    artist_name = song_info['artist']
    tools.addIfTagMissing(tags, 'artist', song_name, artist_name)
    filterIndArtist(tags)