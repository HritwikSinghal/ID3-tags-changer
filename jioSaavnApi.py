import requests
import ssl
import re
import json
from traceback import print_exc
from bs4 import BeautifulSoup as beautifulsoup, BeautifulSoup

from tools import *
from apiKey import getApiKey
from json import JSONDecoder as json_decoder

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def downloadInfo(url):
    # cssPath = ''
    # use getApiKey function to get api key

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }

    res = requests.get(url, headers=user_agent)
    res.raise_for_status()

    print(res.url)

    soup = beautifulsoup(res.text, "html5lib")
    all_songs_info = soup.find_all('div', attrs={"class": "hide song-json"})

    song_list = []

    for info in all_songs_info:
        try:
            songInfo = json.loads(str(info.text))
            x = (json.dumps(songInfo, indent=2))
            print(x)
            break
        except:
            # the error is caused by quotation marks in songs title as shown below
            # (From "XXX")
            # so just remove the whole thing inside parenthesis

            songInfo = re.sub(r'.\(\bFrom .*?"\)', "", str(info.text))
            songInfo = json.loads(str(songInfo))
            x = (json.dumps(songInfo, indent=2))
            print(x)
            break
