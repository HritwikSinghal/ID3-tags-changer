import requests
import shutil
import os

from Base import tools
from mutagen.id3 import ID3, APIC


def addAlbumArt(song_name, song_info, songNameWithPath):
    # for k, v in song_info.items():
    #     print(k, ' ', v)

    url = song_info['image_url'].strip()
    # print(url)

    response = requests.get(url, stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    print("Adding Album Art to", song_name, "...")

    audio = ID3(songNameWithPath)
    with open('img.jpg', 'rb') as albumart:
        audio['APIC'] = APIC(
            encoding=3,
            mime='image/jpeg',
            type=3, desc=u'Cover',
            data=albumart.read()
        )
    audio.save()

    print("Album Art Added.")
    os.remove('img.jpg')


def start(song_name, song_info, songDir, songNameWithPath):
    tools.changeDir(songDir)
    addAlbumArt(song_name, song_info, songNameWithPath)
