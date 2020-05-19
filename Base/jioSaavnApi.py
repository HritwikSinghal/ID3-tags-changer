import json
import re
import ssl
import traceback

import requests
from bs4 import BeautifulSoup as beautifulsoup

from Base import tools

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def fetchList(url, log_file, test=0):
    # cssPath = ''
    # use getApiKey function to get api key

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }

    try:
        res = requests.get(url, headers=user_agent)

        soup = beautifulsoup(res.text, "html5lib")
        all_songs_info = soup.find_all('div', attrs={"class": "hide song-json"})

        song_list = []

        for info in all_songs_info:
            try:
                json_data = json.loads(str(info.text))

                #######################
                # print("IN TRY")
                #######################

                # x = json.dumps(json_data, indent=2)
                # song_list.append(x)

            except:
                # the error is caused by quotation marks in songs title as shown below
                # (foo bar "XXX")
                # so just remove the whole thing inside parenthesis

                #######################
                # print("IN EXCEPT")
                # print(info.text)
                #######################

                try:
                    x = re.compile(r'''
                        (
                        [(\]]
                        .*          # 'featured in' or 'from' or any other shit in quotes
                        "(.*)"      # album name
                        [)\]]
                        )
                        ","album.*"
                        ''', re.VERBOSE)

                    rem_str = x.findall(info.text)

                    # old method, dont know why this wont work
                    # json_data = re.sub(rem_str[0][0], '', str(info.text))

                    json_data = info.text.replace(rem_str[0][0], '')

                    #######################
                    # print(rem_str[0][0])
                    # print(json_data)
                    # a = input()
                    #######################

                    # actually that thing in () is the correct album name, so save it.
                    # since saavn uses song names as album names, this will be useful

                    if len(rem_str[0]) > 1:
                        actual_album = rem_str[0][1]
                    else:
                        actual_album = ''

                except:
                    # old method, if above wont work, this will work 9/10 times.

                    json_data = re.sub(r'.\(\b.*?"\)', "", str(info.text))
                    json_data = re.sub(r'.\[\b.*?"\]', "", json_data)
                    actual_album = ''

                try:
                    json_data = json.loads(str(json_data))
                except:
                    continue
                
                if actual_album != '':
                    json_data['actual_album'] = actual_album

            fix(json_data)
            json_data = json.dumps(json_data, indent=2)

            song_list.append(json_data)

        return song_list
    except:
        print("invalid url...")
        tools.writeAndPrintLog(log_file, "\n\nXXX-------invalid url---------\n", test=test)

        return None


def fix(json_data):
    json_data['album'] = tools.removeGibberish(json_data['album']).strip()

    oldArtist = json_data['singers']
    newArtist = tools.removeGibberish(oldArtist)
    newArtist = tools.divideBySColon(newArtist)
    newArtist = tools.removeTrailingExtras(newArtist)
    json_data['singers'] = tools.removeDup(newArtist)

    old_composer = json_data['music']
    new_composer = tools.removeGibberish(old_composer)
    new_composer = tools.divideBySColon(new_composer)
    new_composer = tools.removeTrailingExtras(new_composer)
    json_data['music'] = tools.removeDup(new_composer)

    json_data['title'] = tools.removeGibberish(json_data['title'])
