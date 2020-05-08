import json
import traceback

from Base import tools
from Base import jioSaavnApi


def getURL(baseUrl, song_name, tags):
    song_name = song_name.lower().strip()

    if tools.isTagPresent(tags, 'album') and tools.removeYear(
            tags['album'][0]).lower().strip() != song_name:

        album = tools.removeYear(tags['album'][0])
        album = tools.removeGibberish(album)
        url = baseUrl + song_name.strip() + ' ' + album

    elif tools.isTagPresent(tags, 'artist'):

        oldArtist = tools.removeGibberish(tags['artist'][0])
        newArtist = tools.divideBySColon(oldArtist)

        newArtist = tools.removeTrailingExtras(newArtist)
        newArtist = tools.removeDup(newArtist)

        url = baseUrl + song_name + ' ' + newArtist

    elif tools.isTagPresent(tags, 'date'):
        url = baseUrl + song_name + ' ' + tags['date'][0]
    else:
        url = baseUrl + song_name
    return url


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
        'actual_album'
    ]

    json_data = json.loads(song_info)
    rinfo = {}

    # for k, v in json_data.items():
    #     print(k, ':', v)

    for key in json_data:

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


def getSong(song_info_list, song_name, tags):
    # automatch song

    for song in song_info_list:
        data = json.loads(song)

        if data['title'].lower().strip() == song_name.lower().strip() and tools.isTagPresent(tags, 'album'):
            if data['album'].lower().strip() == tools.removeYear(tags['album'][0]).lower().strip():
                return song

    #############################
    # print("STOP")
    # x = input()
    #############################

    # if no song was matched, Ask user

    i = 0
    for song in song_info_list:
        rel_keys = getCertainKeys(song)
        print(i + 1, end=' ) \n')
        for key in rel_keys:
            if key != 'actual_album':
                print('\t', key, ':', rel_keys[key])
        print()
        i += 1
    try:
        song_number = int(input("Enter your song number from above list, "
                                "if none matches, enter 'n': ")) - 1
    except IndexError:
        try:
            song_number = int(input("Oops..You mistyped, please enter number within above range\n"
                                    "if none matches, enter 'n': ")) - 1
        except ValueError:
            return -1
    except ValueError:
        return -1

    return song_info_list[song_number]


def start(tags, song_name):
    baseUrl = "https://www.jiosaavn.com/search/"

    url = getURL(baseUrl, song_name, tags)

    ###########################
    print(url)
    # x = input()
    ###########################

    list_of_songs_with_info = jioSaavnApi.fetchList(url)

    ###########################
    # tools.printList(list_of_songs_with_info)
    # x = input()
    ###########################

    song = str(getSong(list_of_songs_with_info, song_name, tags))

    if song == '-1':
        list_of_songs_with_info.clear()

        url = "https://www.jiosaavn.com/search/" + song_name
        list_of_songs_with_info = jioSaavnApi.fetchList(url)
        song = str(getSong(list_of_songs_with_info, song_name, tags))

    song_info = getCertainKeys(song)

    return song_info
