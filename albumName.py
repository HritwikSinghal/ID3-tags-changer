from Base import tools


def modifyAlbum(tags):
    print("Curr Album Name: ", tags['album'][0])

    oldAlbumName = tags['album'][0]
    newName = tools.removeYear(oldAlbumName)
    newName = tools.removeGibberish(newName)

    newAlbumName = newName + ' (' + tags['date'][0] + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", newAlbumName)


def start(tags, song_name, album_name):
    tools.addIfTagMissing(tags, 'album', song_name, album_name)
    modifyAlbum(tags)

