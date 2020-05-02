import requests, ssl, re, html5lib
from bs4 import BeautifulSoup as beautifulsoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getTags(tags):
    url = 'https://www.jiosaavn.com/search/'
    content = requests.get(url).content
    soup = beautifulsoup(content, "html5lib")


def start(tags):
    getTags(tags)
