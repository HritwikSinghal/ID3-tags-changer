import re
from traceback import print_exc
import json
from json import JSONDecoder as jsondecoder

import tools
import jioSaavnApi


def getTags(songTags, song_name, tag_name='none'):
    baseUrl = "https://www.jiosaavn.com/search/"
    number = 1

    if tools.isTagPresent(songTags, 'album') and \
            tools.removeYear(songTags['album'][0]) != song_name and tag_name != 'album':
        url = baseUrl + song_name + ' ' + songTags['album'][0]
        song_list = jioSaavnApi.fetchInfo(url, number)

    elif tools.isTagPresent(songTags, 'artist'):
        url = baseUrl + songTags['title'][0] + ' ' + tools.removeGibberish(songTags['artist'][0])
        song_list = jioSaavnApi.fetchInfo(url, number)

    else:
        # todo : show list of songs and make user select from it
        url = ''
        number = 5
        song_list = jioSaavnApi.fetchInfo(url, number)

    song_info = song_list[0]
    print(song_info)

    if tag_name == 'none':
        pass
    else:
        pass


def start(tags, song_name, tag_name='none'):
    getTags(tags, song_name, tag_name)
