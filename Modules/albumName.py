from Base import tools


def fixAlbum(tags, json_data):
    print("Curr Album Name: ", tags['album'][0])

    oldAlbumName = tags['album'][0]
    newName = tools.removeYear(oldAlbumName)
    newName = tools.removeGibberish(newName)

    newAlbumName = newName + ' (' + json_data['date'] + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", newAlbumName)


def start(tags, json_data):
    album_name = json_data['album']
    tools.checkAndFixTag(tags, 'album', album_name)
    fixAlbum(tags, json_data)
