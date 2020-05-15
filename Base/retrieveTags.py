import json
import traceback

from Base import tools
from Base import jioSaavnApi


def getURL(baseUrl, song_name, tags):
    # get the search url using album or artist or year or only name

    song_name = song_name.lower().strip()

    if tools.isTagPresent(tags, 'album') and \
            tools.removeYear(tags['album'][0]).lower().strip() != song_name:

        album = tools.removeYear(tags['album'][0]).lower().strip()
        album = tools.removeGibberish(album)

        url = baseUrl + song_name + ' ' + album

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
    # these are the keys which are useful to us

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

    # this will store all relevant keys and their values
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


def getSong(song_info_list, song_name, tags, bit=0):
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

    if bit == 1:
        print('\n------------------------------------------------------\nEnter number from below...')
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
        if bit == 1:
            song_number = int(input("\nI've searched again! Please enter your song number from above list,\n"
                                    "if none matches, enter 'n': ")) - 1
        else:
            song_number = int(input("\nEnter your song number from above list, "
                                    "if none matches, enter 'n': ")) - 1
    except IndexError:
        try:
            song_number = int(input("\nOops..You mistyped, please enter number within above range\n"
                                    "if none matches, enter 'n': ")) - 1
        except ValueError:
            return -1
    except ValueError:
        return -1

    return song_info_list[song_number]


def start(tags, song_name, test=0):
    baseUrl = "https://www.jiosaavn.com/search/"

    url = getURL(baseUrl, song_name, tags)
    if test:
        print(url)
        # x = input()

    # get a list of songs which match search
    list_of_songs_with_info = jioSaavnApi.fetchList(url)

    ###########################
    # tools.printList(list_of_songs_with_info)
    # x = input()
    ###########################

    if len(list_of_songs_with_info) != 0:
        # means songs were found! move to getting the correct song from that list
        song = getSong(list_of_songs_with_info, song_name, tags)
    else:
        # retry, but search only using song name
        print("Oops...Couldn't find the song in this turn, let me retry :p ..... ")
        song = -1

    # retry, but search only using song name
    if song == -1:
        list_of_songs_with_info.clear()
        url = baseUrl + song_name

        if test:
            print(url)

        list_of_songs_with_info = jioSaavnApi.fetchList(url)
        song = getSong(list_of_songs_with_info, song_name, tags, 1)

    if song == -1:
        return

    # the info we got had too much info, we will save only certain keys like artist from it
    song_info = getCertainKeys(song)

    # return those selected keys
    return song_info


# todo: fix below
'''
Traceback (most recent call last):
Traceback (most recent call last):
File "E:\Py_proj\Music-library-repairer\Modules\main.py", line 99, in fixTags
json_data = retrieveTags.start(tags, song_name, test=test)
File "E:\Py_proj\Music-library-repairer\Base\retrieveTags.py", line 167, in start
song_info = getCertainKeys(song)
File "E:\Py_proj\Music-library-repairer\Base\retrieveTags.py", line 64, in getCertainKeys
for key in json_data:
TypeError: 'int' object is not iterable
'''
