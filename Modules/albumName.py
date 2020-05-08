from Base import tools


def fixAlbum(tags, date):
    print("Curr Album Name: ", tags['album'][0])

    oldAlbumName = tags['album'][0]
    newName = tools.removeYear(oldAlbumName)
    newName = tools.removeGibberish(newName)

    newAlbumName = newName + ' (' + date + ')'

    if oldAlbumName != newAlbumName:
        tags['album'] = newAlbumName
        tags.save()
        print("New Album Name : ", newAlbumName)


def start(tags, json_data, found_data):
    if found_data:
        try:
            album_name = json_data['actual_album']
        except KeyError:
            album_name = json_data['album']

        tools.checkAndFixTag(tags, 'album', album_name)
        date = json_data['date']
        fixAlbum(tags, date)

    else:
        date = tags['date'][0]
        fixAlbum(tags, date)
