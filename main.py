# import requests, os, ssl, re, html5lib
# from bs4 import BeautifulSoup as beautifulsoup
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# os.chdir(r'C:\Users\hritwik\Desktop')
# # print(os.getcwd())
#
# file = open("data.txt", 'w+', encoding='utf-8')
#
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#
# soup = beautifulsoup(requests.get(url).content, "html5lib")
#
# tags = soup.find_all('a')
# print(type(tags))
# # for tag in tags:
# #     print(tag['href'])
# # print(re.findall('known_by_(.+)\.html', tags[-1]['href']))

import os, re, traceback
import albumName, artistName, composerName, songName, songTitle
from listPrint import print_list


def takeDir():
    # songDir = input("enter song dir:  ")
    songDir = r'C:\Users\hritwik\Pictures\Camera Roll'

    print("Song dir is: ", songDir)
    return songDir


def addFullPath(songDir):
    files_in_dir = os.listdir(songDir)

    full_path_of_songs = []
    for song_name in files_in_dir:
        song_name = re.findall(r'(.+\.mp3)', song_name)
        if len(song_name) != 0:
            name = os.path.join(songDir, song_name[0])
            full_path_of_songs.append(name)
    return full_path_of_songs


def change(songDir):
    full_path_of_songs = addFullPath(songDir)
    print('Now in ', songDir, ' and: ')
    try:
        # artistName.start(full_path_of_songs)
        # composerName.start(full_path_of_songs)
        albumName.start(full_path_of_songs)
        # full_path_of_songs = songName.start(full_path_of_songs)
        # songTitle.start()
        print()
    except Exception:
        print(traceback.format_exc())


def start():
    # taking songs directory
    songDir = takeDir()

    # resp = input("\nDo you want walk down?\ny == Yes, n == No\n") == 'y'
    resp = False
    if resp:
        print("walking down ", songDir, "...")
        for dirPath, subDirName, fileNames in (os.walk(songDir, topdown=True)):
            songDir = dirPath
            change(songDir)
    else:
        print("Only changinig attributes in: ", songDir, " Dir...\n")
        change(songDir)


start()

# ex = 'Samuel &amp; Akanksha/Samuel &amp; Akanksha &amp; Jubin Nautiyal/Jubin Nautiyal'

# print(re.findall(r'', ex))
