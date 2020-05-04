import requests
import ssl
import re
import json
from traceback import print_exc
from bs4 import BeautifulSoup as beautifulsoup, BeautifulSoup

from tools import *
from jioSaavnApi import *
from apiKey import getApiKey
from json import JSONDecoder as json_decoder

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getTags(songTags, tagName='def'):
    baseUrl = "https://www.jiosaavn.com/search/"
    if songTags['album'][0] != songTags['title'][0]:
        url = baseUrl + songTags['title'][0] + ' ' + songTags['album'][0]
    else:
        url = baseUrl + songTags['title'][0] + ' ' + songTags['artist'][0]

    downloadInfo(url)


def start(tags):
    getTags(tags)
