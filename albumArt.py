# method 1 link: https://stackoverflow.com/questions/42473832/embed-album-cover-to-mp3-with-mutagen-in-python-3
# method 2 link: https://stackoverflow.com/questions/42665036/python-mutagen-add-image-cover-doesnt-work

import requests
import shutil
import os

from Base import tools
from mutagen.id3 import ID3, APIC, TIT2


def addAlbumArt(song_name, song_info, songNameWithPath):
    # for k, v in song_info.items():
    #     print(k, ' ', v)

    url = song_info['image_url'].strip()

    # Download AlbumArt
    response = requests.get(url, stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    print("Adding Album Art to", song_name, "...")

    # Add Album Art
    audio = ID3(songNameWithPath)
    with open('img.jpg', 'rb') as albumart:
        # method 1
        audio['APIC'] = APIC(
            encoding=3,
            mime='image/jpeg',
            type=3, desc='Cover',
            data=albumart.read()
        )
        audio.save(v2_version=3)

        # if we save like below, win explorer wont recognize albumArt
        # since it uses v2.3 tags and ID3 saves v2.4.
        # audio.save()

        # # method 2
        # audio.add(APIC(
        #     encoding=3,
        #     mime='image/jpeg',
        #     type=3,
        #     desc='Cover',
        #     data=albumart)
        # )
        # audio.add(TIT2(
        #     encoding=3,
        #     text='title')
        # )
        # audio.save(v2_version=3)

    print("Album Art Added.")
    os.remove('img.jpg')


def start(song_name, song_info, songDir, songNameWithPath):
    tools.changeDir(songDir)
    addAlbumArt(song_name, song_info, songNameWithPath)
