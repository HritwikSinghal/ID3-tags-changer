# This was a major help
# https://stackoverflow.com/questions/42231932/writing-id3-tags-using-easyid3

from mutagen.easyid3 import EasyID3 as easyid3
from os.path import isfile
from traceback import print_exc

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
from Base.tools import printList
from Base import retrieveTags


def inputSongDir(test=0):
    while True:
        if test == 1:
            songDir = r'C:\Users\hritwik\Pictures\Camera Roll'
        else:
            songDir = input("Enter song dir:  ")

        if os.path.isdir(songDir):
            print("Song dir is: ", songDir)
            return songDir
        else:
            print("No such Dir exist, Please enter Dir again...")


def getSongList(files):
    songs = []
    for x in files:
        x = tools.re.findall(r'(.+\.mp3)', x)
        if len(x) != 0:
            # name = tools.os.path.join(files, x[0])
            # songs.append(name)
            songs.append(x[0])
    return songs


def changeSongName(songDir, song_list):
    print("Fixing song names....")

    for song in song_list:
        songName.start(songDir, song, song_list)
        print()
    print()


def handleSongs(song_dir, files, flag=1):
    print('Now in ', song_dir)

    # Ask user permission to fix songs in curr dir if flag is set to 0
    if flag == 0:
        if int(input("Do you Want to Fix songs in " + song_dir + " ?\n1 == Yes, 0 == NO\n")) == 0:
            return

    song_list = getSongList(files)

    # fix song name
    try:
        changeSongName(song_dir, song_list)
    except:
        print("XXX---There Was some error fixing this tag. Moving to next")
        print_exc()

    # fix tags
    for song in song_list:
        song_with_path = tools.join(song_dir, song)

        try:
            tags = easyid3(song_with_path)
        except:
            print("This Song has no tags. Creating tags...")

            tags = mutagen.File(song_with_path, easy=True)
            tags.add_tags()

            print("Tags created.")

        song_name = tools.removeBitrate(song)
        song_name = song_name.replace('.mp3', '')
        song_name = song_name.strip()

        print("Song Name: ", song_name)
        try:
            json_data = retrieveTags.start(tags, song_name)
            found_data = 1
        except:
            found_data = 0
            json_data = ''
            print("Cannot find data for selected song. Fixing tags locally")
            print_exc()

        #
        #
        try:
            albumName.start(tags, json_data, found_data)
        except:
            print("XXX---There Was some error fixing this tag.\n"
                  "Make sure year is there in song tags. if not,"
                  "add it manually and re-run this program.\n"
                  "Moving to next")
            print_exc()
        try:
            artistName.start(tags, json_data, found_data)
        except:
            print("XXX---There Was some error fixing this tag. Moving to next")
            print_exc()
        try:
            composerName.start(tags, json_data, found_data)
        except:
            print("XXX---There Was some error fixing this tag. Moving to next")
            print_exc()

        try:
            songTitle.start(tags, json_data, found_data)
        except:
            print("XXX---There Was some error fixing this tag. Moving to next")
            print_exc()

        try:
            addDateLenOrg.start(tags, json_data, found_data)
        except:
            print("XXX---There Was some error fixing this tag. Moving to next")
            print_exc()

        try:
            albumArt.start(json_data, song_dir, song_with_path, found_data)
        except:
            print("XXX---There Was some error fixing this tag. Moving to next")
            print_exc()

        print()


def start(test=0):
    song_dir = inputSongDir(test)

    if test == 1:
        flag = -1
    else:
        flag = int(input("\nDo you want to run in all sub-dirs?\n"
                         "1 == Yes,\n-1 == No,\n0 == Ask in each Dir\n"))

    if flag == -1:
        print("Only changing attributes in:", song_dir, "...\n")

        files = [
            x
            for x in os.listdir(song_dir)
            if isfile(tools.join(song_dir, x))
        ]

        handleSongs(song_dir, files)

    else:
        print("Walking down ", song_dir, "\b...")
        for curr_dir, sub_dirs, files in tools.os.walk(song_dir, topdown=True):
            handleSongs(curr_dir, files, flag)
