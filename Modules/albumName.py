from Base import tools


def modifyAlbum(tags, song_info):
    print("Curr Album Name: ", tags['album'][0])

    oldAlbumName = tags['album'][0]
    newName = tools.removeYear(oldAlbumName)
    newName = tools.removeGibberish(newName)

    newAlbumName = newName + ' (' + song_info['date'] + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", newAlbumName)


def start(tags, song_name, song_info):
    album_name = song_info['album']
    tools.addIfTagMissing(tags, 'album', song_name, album_name)
    modifyAlbum(tags, song_info)
