# import json
# import re
# import ssl
# import traceback
#
# import requests
# from bs4 import BeautifulSoup as beautifulsoup
#
# from Base import tools
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
#     'referer': 'https://www.jiosaavn.com/song/tere-naal/KD8zfAZpZFo',
#     'origin': 'https://www.jiosaavn.com'
# }
#
#
# def fetchList(url, log_file, test=0):
#     # cssPath = ''
#
#     try:
#         res = requests.get(url, headers=headers)
#
#         soup = beautifulsoup(res.text, "html5lib")
#         all_songs_info = soup.find_all('div', attrs={"class": "hide song-json"})
#
#         song_list = []
#
#         for info in all_songs_info:
#             try:
#                 json_data = json.loads(str(info.text))
#
#                 #######################
#                 # print("IN TRY")
#                 #######################
#
#                 # x = json.dumps(json_data, indent=2)
#                 # song_list.append(x)
#
#             except:
#                 # the error is caused by quotation marks in songs title as shown below
#                 # (foo bar "XXX")
#                 # so just remove the whole thing inside parenthesis
#
#                 #######################
#                 # print("IN EXCEPT")
#                 # print(info.text)
#                 #######################
#
#                 try:
#                     x = re.compile(r'''
#                         (
#                         [(\]]
#                         .*          # 'featured in' or 'from' or any other shit in quotes
#                         "(.*)"      # album name
#                         [)\]]
#                         )
#                         ","album.*"
#                         ''', re.VERBOSE)
#
#                     rem_str = x.findall(info.text)
#
#                     # old method, dont know why this wont work
#                     # json_data = re.sub(rem_str[0][0], '', str(info.text))
#
#                     json_data = info.text.replace(rem_str[0][0], '')
#
#                     #######################
#                     # print(rem_str[0][0])
#                     # print(json_data)
#                     # a = input()
#                     #######################
#
#                     # actually that thing in () is the correct album name, so save it.
#                     # since saavn uses song names as album names, this will be useful
#
#                     if len(rem_str[0]) > 1:
#                         actual_album = rem_str[0][1]
#                     else:
#                         actual_album = ''
#
#                 except:
#                     # old method, if above wont work, this will work 9/10 times.
#
#                     json_data = re.sub(r'.\(\b.*?"\)', "", str(info.text))
#                     json_data = re.sub(r'.\[\b.*?"\]', "", json_data)
#                     actual_album = ''
#
#                 try:
#                     json_data = json.loads(str(json_data))
#                 except:
#                     continue
#
#                 if actual_album != '':
#                     json_data['actual_album'] = actual_album
#
#             fix(json_data)
#             json_data = json.dumps(json_data, indent=2)
#
#             song_list.append(json_data)
#
#         return song_list
#     except:
#         print("invalid url...")
#         tools.writePrintLog(log_file, "\n\nXXX-------invalid url---------\n", test=test)
#
#         return None
#
#
# def fix(json_data):
#     json_data['album'] = tools.removeGibberish(json_data['album']).strip()
#
#     oldArtist = json_data['singers']
#     newArtist = tools.removeGibberish(oldArtist)
#     newArtist = tools.divideBySColon(newArtist)
#     newArtist = tools.removeTrailingExtras(newArtist)
#     json_data['singers'] = tools.removeDup(newArtist)
#
#     old_composer = json_data['music']
#     new_composer = tools.removeGibberish(old_composer)
#     new_composer = tools.divideBySColon(new_composer)
#     new_composer = tools.removeTrailingExtras(new_composer)
#     json_data['music'] = tools.removeDup(new_composer)
#
#     json_data['title'] = tools.removeGibberish(json_data['title'])


import json
import re

import requests
import urllib3.exceptions

from Base import tools

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'referer': 'https://www.jiosaavn.com/song/tere-naal/KD8zfAZpZFo',
    'origin': 'https://www.jiosaavn.com'
}

search_api_url = 'https://www.jiosaavn.com/api.php?p=1&q={0}&_format=json&_marker=0&api_version=4&ctx=web6dot0&n=20&__call=search.getResults'


def printText(text, test=0):
    if test:
        print(text)


def getURL(baseUrl, song_name, tags):
    # get the search url using album or artist or year or only name

    song_name = song_name.lower().strip()

    if tools.isTagPresent(tags, 'album') and \
            tools.removeYear(tags['album'][0]).lower().strip() != song_name:

        album = tools.removeYear(tags['album'][0]).lower().strip()
        album = tools.removeGibberish(album)

        url = baseUrl.format(song_name + ' ' + album)

    elif tools.isTagPresent(tags, 'artist'):

        oldArtist = tools.removeGibberish(tags['artist'][0])
        newArtist = tools.divideBySColon(oldArtist)

        newArtist = tools.removeTrailingExtras(newArtist)
        newArtist = tools.removeDup(newArtist)

        url = baseUrl.format(song_name + ' ' + newArtist)

    elif tools.isTagPresent(tags, 'date'):
        url = baseUrl.format(song_name + ' ' + tags['date'][0])
    else:
        url = baseUrl.format(song_name)
    return url.replace(" ", '+')


def fix(song_info, test=0):
    oldArtist = song_info["primary_artists"]
    newArtist = tools.removeGibberish(oldArtist)
    newArtist = tools.divideBySColon(newArtist)
    newArtist = tools.removeTrailingExtras(newArtist)
    song_info['primary_artists'] = tools.removeDup(newArtist)

    song_info["singers"] = song_info['primary_artists']

    old_composer = song_info["music"]
    new_composer = tools.removeGibberish(old_composer)
    new_composer = tools.divideBySColon(new_composer)
    new_composer = tools.removeTrailingExtras(new_composer)
    song_info["music"] = tools.removeDup(new_composer)

    song_info['image'] = song_info['image'].replace('-150x150.jpg', '-500x500.jpg')

    # ---------------------------------------------------------------#

    new_title = song_info['title'].replace('&quot;', '#')
    if new_title != song_info['title']:
        song_info['title'] = new_title
        song_info['title'] = tools.removeGibberish(song_info['title'])

        x = re.compile(r'''
                                (
                                [(\]]
                                .*          # 'featured in' or 'from' or any other shit in quotes
                                \#(.*)\#      # album name
                                [)\]]
                                )
                                ''', re.VERBOSE)

        album_name = x.findall(song_info['title'])
        song_info['title'] = song_info['title'].replace(album_name[0][0], '').strip()

        song_info['album'] = album_name[0][1]

        # old method, if above wont work, this will work 9/10 times.
        # json_data = re.sub(r'.\(\b.*?"\)', "", str(info.text))
        # json_data = re.sub(r'.\[\b.*?"\]', "", json_data)
        # actual_album = ''

    song_info['title'] = tools.removeGibberish(song_info['title'])
    song_info["album"] = tools.removeGibberish(song_info["album"]).strip()
    song_info["album"] = song_info["album"] + ' (' + song_info['year'] + ')'

    if test:
        print(json.dumps(song_info, indent=2))


def getImpKeys(song_info, log_file, test=0):
    keys = {}

    keys["title"] = song_info["title"]
    keys["primary_artists"] = ", ".join(
        [artist["name"] for artist in song_info["more_info"]["artistMap"]["primary_artists"]])
    keys["album"] = song_info["more_info"]["album"]
    keys["singers"] = keys["primary_artists"]
    keys["music"] = song_info["more_info"]["music"]
    keys["starring"] = ";".join(
        [artist["name"] for artist in song_info["more_info"]["artistMap"]["artists"] if artist['role'] == 'starring'])
    keys['year'] = song_info['year']
    keys["label"] = song_info["more_info"]["label"]
    keys['image'] = song_info['image']
    keys['encrypted_media_url'] = song_info['more_info']['encrypted_media_url']

    fix(keys, test=test)

    return keys


def fixContent(data):
    # old
    # data = re.sub(r'<!DOCTYPE html>\s*<.*>?', '', data)
    # return data

    fixed_json = [x for x in data.splitlines() if x.strip().startswith('{')][0]
    return fixed_json


def start(song_name, tags, log_file, test=0):
    url = getURL(search_api_url, song_name, tags)
    printText(url, test=test)
    res = requests.get(url, headers=headers)

    data = str(res.text).strip()
    try:
        data = json.loads(data)
    except:
        data = fixContent(data)
        data = json.loads(data)

    # todo: remove this
    # -------------------------------------------------- #
    with open('song.txt', 'w+', encoding='utf-8') as aaa:
        json.dump(data, aaa, indent=4)

    print(data['results'])

    if test:
        x = input()
    # -------------------------------------------------- #

    # if songs were found, get imp keys of songs
    songs_info = []
    if int(data['total']) != 0:
        retry_flag = 0
        for curr_song in data['results']:
            songs_info.append(getImpKeys(curr_song, log_file, test=test))

    # else set retry flag to -1 so we can retry below
    else:
        print("Oops...Couldn't find the song in this turn, let me retry :p ..... ")
        retry_flag = -1

    # if retry flag is -1, search only using song name
    # this flag was set by us if no songs were found in first try
    # or it may be set by user when there are no matching songs in the list
    # (the getSongs function returns -1 if user inputs 'n'
    # in both cases, we have to retry search using song name

    if retry_flag == -1:
        songs_info.clear()

        # new url based only on song name
        url = search_api_url + song_name
        printText(url, test=test)

        list_of_songs_with_info = jioSaavnApi.start(url, tags, log_file, test=test)

        # None can only be returned in case of any error, so we were not able to find data
        if list_of_songs_with_info is None:
            return None

        song = getSong(list_of_songs_with_info, song_name, tags, song_with_path, test)

    # if we were still not able to find correct song in 2nd try, just return None
    # (means we failed to find data about song)
    if retry_flag == -1:
        return None

    # if the song was found in any of above cases, then we go below.
    # the info we got had too much info, we will save only certain keys like artist from it
    song_info = getCertainKeys(retry_flag)

    # -------------------------------------------------- #
    return data
