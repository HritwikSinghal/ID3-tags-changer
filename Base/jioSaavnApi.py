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

    # todo: remove this
    # -------------------------------------------------- #
    data = json.loads(res.text.strip())
    with open('song.txt', 'w+', encoding='utf-8') as aaa:
        json.dump(data, aaa, indent=4)
    print(data['results'][0])

    if test:
        x = input()
    # -------------------------------------------------- #

    data = str(res.text).strip()

    try:
        data = json.loads(data)
    except:
        data = fixContent(data)
        data = json.loads(data)

    return data
