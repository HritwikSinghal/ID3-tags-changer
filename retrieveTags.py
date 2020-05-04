import requests
import ssl
import re
import json
from bs4 import BeautifulSoup as beautifulsoup

from tools import *
from apiKey import getApiKey
from json import JSONDecoder as json_decoder

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getTags(songTags):
    # cssPath = ''
    # use getApiKey function to get api key

    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
    baseUrl = "https://www.jiosaavn.com/search/"

    url = baseUrl + songTags['title'][0]
    # url = "https://www.jiosaavn.com/search/" + 'bhula dunga'

    # res = requests.get(url, headers=user_agent, data=[('bitrate', '320')])
    res = requests.get(url, headers=user_agent)
    res.raise_for_status()
    print(res.url)

    soup = beautifulsoup(res.text, "html5lib")
    all_song_divs = soup.find_all('div', attrs={"class": "hide song-json"})

    songs = []

    for info in all_song_divs:
        try:
            songInfo = json.loads(str(info.text))
            print(json.dumps(songInfo, indent=2))
        except:
            songInfo = re.sub(r'.\(\bFrom .*?"\)', "", str(info.text))
            print('for this, above failed')

            songInfo = json.dumps(str(songInfo))
            print(songInfo)

def start(tags):
    getTags(tags)
