# This was a major help
# https://stackoverflow.com/questions/42231932/writing-id3-tags-using-easyid3

from mutagen.easyid3 import EasyID3 as easyid3

import os
import mutagen

from Modules import albumName
from Modules import artistName
from Modules import composerName
from Modules import songTitle
from Modules import songName
from Modules import addDateLenOrg
from Modules import albumArt

from Base import tools
from Base import retrieveTags


def inputSongDir():
    while True:
        # songDir = input("Enter song dir:  ")
        songDir = r'C:\Users\hritwik\Pictures\Camera Roll'

        if os.path.isdir(songDir):
            print("Song dir is: ", songDir)
            return songDir
        else:
            print("No such Dir exist, Please enter again...")


def getFullPathOfSongsInDir(songDir):
    files_in_dir = tools.os.listdir(songDir)

    full_path_of_songs = []
    for song_name in files_in_dir:
        song_name = tools.re.findall(r'(.+\.mp3)', song_name)
        if len(song_name) != 0:
            name = tools.os.path.join(songDir, song_name[0])
            full_path_of_songs.append(name)
    return full_path_of_songs


def changeSongName(songDir, full_path_of_songs):
    print("Fixing song names....")
    for songNameWithPath in full_path_of_songs:
        songName.start(songDir, full_path_of_songs, songNameWithPath)
    print()


def handleSongs(songDir, flag=1):
    full_path_of_songs = getFullPathOfSongsInDir(songDir)
    print('Now in ', songDir)

    # Ask user permission to fix songs in curr dir
    if flag == 0:
        if int(input("Do you Want to Fix songs in " + songDir + " ?\n1 == Yes, 0 == NO\n")) == 0:
            return

    # fix song name
    # changeSongName(songDir, full_path_of_songs)

    # Change song tags
    for songNameWithPath in full_path_of_songs:
        try:
            tags = easyid3(songNameWithPath)
        except:
            print("This file has no tags. Creating tags...")

            tags = mutagen.File(songNameWithPath, easy=True)
            tags.add_tags()

            print("Tags created.")

        song_name = tools.getSongNameWithoutPath(songNameWithPath)
        song_name = tools.removeBitrate(song_name)
        song_name = song_name.replace('.mp3', '')
        song_name = song_name.strip()

        print("Song Name: ", song_name)

        # song_info = retrieveTags.start(tags, song_name)
        #
        # # for k, v in song_info.items():
        # #     print(k, " ", v)
        #
        # albumName.start(tags, song_name, song_info)
        # artistName.start(tags, song_name, song_info)
        # composerName.start(tags, song_name, song_info)
        # songTitle.start(tags, song_name, song_info)
        #
        # addDateLenOrg.start(tags, song_name, song_info)
        # albumArt.start(song_name, song_info, songDir, songNameWithPath)
        #
        # print()


def start():
    # input songs directory
    all_song_dir = inputSongDir()

    # walk_down_curr_dir = input("\nDo you want to run in all sub-dirs?\n"
    #                            "1 == Yes,\n-1 == No,\n0 == Some (Will ask in each Dir)\n")
    walk_down_curr_dir = -1
    if walk_down_curr_dir != -1:
        print("Walking down ", all_song_dir, "\b...")
        for dirPath, subDirName, fileNames in tools.os.walk(all_song_dir, topdown=True):
            curr_songs_dir = dirPath
            handleSongs(curr_songs_dir, int(walk_down_curr_dir))
    else:
        print("Only changing attributes in: ", all_song_dir, "...\n")
        handleSongs(all_song_dir)
