import os, re, traceback
import albumName, artistName, composerName, songName, songTitle
from mutagen.easyid3 import EasyID3 as easyid3
from tools import *


def inputSongDir():
    # songDir = input("Enter song dir:  ")
    songDir = r'C:\Users\hritwik\Pictures\Camera Roll'

    print("Song dir is: ", songDir)
    return songDir


def getFullPath(songDir):
    files_in_dir = os.listdir(songDir)

    full_path_of_songs = []
    for song_name in files_in_dir:
        song_name = re.findall(r'(.+\.mp3)', song_name)
        if len(song_name) != 0:
            name = os.path.join(songDir, song_name[0])
            full_path_of_songs.append(name)
    return full_path_of_songs


def changeSongTags(songNameWithPath, tags, songDir, full_path_of_songs):
    artistName.start(tags)
    albumName.start(tags)
    composerName.start(tags)
    songName.start(songDir, full_path_of_songs, songNameWithPath)
    # songTitle.start(tags)
    print()


def handleSongs(songDir):
    full_path_of_songs = getFullPath(songDir)
    print('Now in ', songDir)

    for songNameWithPath in full_path_of_songs:
        tags = easyid3(songNameWithPath)
        print("Song title: ", tags['title'][0])
        changeSongTags(songNameWithPath, tags, songDir, full_path_of_songs)


def start():
    # taking songs directory
    songDir = inputSongDir()

    # resp = input("\nDo you want walk down?\n1 == Yes, 0 == No\n") == '1'
    resp = False
    if resp:
        print("Walking down ", songDir, "...")
        for dirPath, subDirName, fileNames in (os.walk(songDir, topdown=True)):
            songDir = dirPath
            handleSongs(songDir)
    else:
        print("Only changing attributes in: ", songDir, "...\n")
        handleSongs(songDir)


start()

# ex = 'Samuel &amp; Akanksha/Samuel &amp; Akanksha &amp; Jubin Nautiyal/Jubin Nautiyal'
# print(re.findall(r'', ex))
