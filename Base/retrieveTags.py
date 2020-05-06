import json

from Base import tools
from Base import jioSaavnApi


def getCertainKeys(song_info):
    rel_keys = [
        'title',
        'album',
        'singers',
        'music',

        'year',
        'label',
        'duration',

        'e_songid',
        'image_url',
    ]

    json_data = json.loads(song_info)
    rinfo = {}

    for key in json_data:
        # print(key, " ", json_data[key])

        if key in rel_keys:
            if key == 'singers':
                rinfo['artist'] = json_data[key]
            elif key == 'music':
                rinfo['composer'] = json_data[key]
            elif key == 'year':
                rinfo['date'] = json_data[key]
            elif key == 'duration':
                rinfo['length'] = json_data[key]
            elif key == 'label':
                rinfo['organization'] = json_data[key]
            elif key == 'image_url':
                rinfo['image_url'] = tools.fixImageUrl(json_data[key])

            else:
                rinfo[key] = json_data[key]

    return rinfo


def getTags(tags, song_name):
    baseUrl = "https://www.jiosaavn.com/search/"
    max_songs_to_show = 1
    song_number = 0

    # Search using album tag
    if tools.isTagPresent(tags, 'album') and \
            tools.removeYear(tags['album'][0]) != song_name:
        url = baseUrl + song_name + ' ' + tags['album'][0]
        song_list = jioSaavnApi.fetchInfo(url, max_songs_to_show)

    # search using artist tag if no album tag or
    # both album and song name are same
    elif tools.isTagPresent(tags, 'artist'):
        url = baseUrl + song_name + ' ' + tools.removeGibberish(tags['artist'][0])
        song_list = jioSaavnApi.fetchInfo(url, max_songs_to_show)

    # show list of songs and make user select from it
    else:
        url = baseUrl + song_name
        max_songs_to_show = 5
        song_list = jioSaavnApi.fetchInfo(url, max_songs_to_show)

        i = 0
        for each_song in song_list:
            song_info = getCertainKeys(each_song)
            print(i + 1, end=' ) \n')
            for key in song_info:
                print('\t', key, ': ', song_info[key])
            print()
            i += 1

        song_number = int(input("Enter your song number from above list: ")) - 1

    # get all the details of chosen song
    full_song_info = song_list[song_number]

    # get useful details of chosen song
    song_info = getCertainKeys(full_song_info)

    return song_info


def start(tags, song_name):
    return getTags(tags, song_name)
