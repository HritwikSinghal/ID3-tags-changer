import re
from traceback import print_exc
import json
from json import JSONDecoder as jsondecoder

import tools
import jioSaavnApi


def getCertainKeys(song_info):
    rel_keys = [
        'title',
        'album',
        'singers',
        'music',
        'year',
        'label',

        'e_songid',
        'image_url',
    ]

    info = json.loads(song_info)
    rinfo = {}

    for key in info:
        if key in rel_keys:
            if key == 'singers':
                rinfo['artist'] = info[key]
            elif key == 'music':
                rinfo['composer'] = info[key]
            else:
                rinfo[key] = info[key]

    # for x in rinfo:
    #     print(x, ': ', rinfo[x])

    return rinfo


def getTags(songTags, song_name, tag_name='none'):
    baseUrl = "https://www.jiosaavn.com/search/"
    number = 1

    song_name = tools.removeBitrate(song_name)
    song_number = 0

    if tools.isTagPresent(songTags, 'album') and \
            tools.removeYear(songTags['album'][0]) != song_name and tag_name != 'album':
        url = baseUrl + song_name + ' ' + songTags['album'][0]
        song_list = jioSaavnApi.fetchInfo(url, number)

    elif tools.isTagPresent(songTags, 'artist'):
        url = baseUrl + songTags['title'][0] + ' ' + tools.removeGibberish(songTags['artist'][0])
        song_list = jioSaavnApi.fetchInfo(url, number)

    else:
        # todo : show list of songs and make user select from it
        url = baseUrl + song_name
        number = 5
        song_list = jioSaavnApi.fetchInfo(url, number)

        i = 0
        for each_song in song_list:
            soin = getCertainKeys(each_song)
            print(i, end=' ) \n')
            for key in soin:
                print('\t', key, ': ', soin[key])
            print()
            i += 1

        song_number = int(input("Enter your song number from above list: "))

    full_song_info = song_list[song_number]

    song_info = getCertainKeys(full_song_info)
    # print(song_info)

    if tag_name == 'none':
        # todo : implement this
        pass
    else:
        songTags[tag_name] = song_info[tag_name]
        songTags.save()


def start(tags, song_name, tag_name='none'):
    getTags(tags, song_name, tag_name)
