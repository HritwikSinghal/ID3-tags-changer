import requests, ssl, re, html5lib
from bs4 import BeautifulSoup as beautifulsoup

from tools import *

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getTags(songTags):
    baseUrl = 'https://www.jiosaavn.com/search/'

    # url = baseUrl + songTags['title'][0]
    url = 'https://www.flipkart.com/fortune-sunlite-refined-sunflower-oil-pouch/p/itmf8phyytkfbuy7'

    r = requests.get(url)
    r.raise_for_status()

    soup = beautifulsoup(r.text, "html5lib")
    # cssPath = ''

    cssPath = 'html.fonts-loaded body div#container div div.t-0M7P._3GgMx1._2doH3V div._3e7xtJ div._1HmYoV.hCUpcT div._1HmYoV._35HD7C.col-8-12 div.bhgxx2.col-12-12 div._29OxBi div._3iZgFn div._2i1QSc div._1uv9Cb div._1vC4OE._3qQ9m1'

    x = soup.select(cssPath)
    print(x)
    # x = soup.find_all('a')
    # # printList(x)
    # for a in x:
    #     if a.get('href') is not None:
    #         print(a.get('href'))


def start(tags):
    getTags(tags)
