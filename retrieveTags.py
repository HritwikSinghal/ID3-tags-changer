import requests, os, ssl, re, html5lib
from bs4 import BeautifulSoup as beautifulsoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

os.chdir(r'C:\Users\hritwik\Desktop')
# print(os.getcwd())

file = open("data.txt", 'w+', encoding='utf-8')

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

soup = beautifulsoup(requests.get(url).content, "html5lib")

tags = soup.find_all('a')
print(type(tags))
# for tag in tags:
#     print(tag['href'])
# print(re.findall('known_by_(.+)\.html', tags[-1]['href']))
