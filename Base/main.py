# This was a major help
# https://stackoverflow.com/questions/42231932/writing-id3-tags-using-easyid3

import os
import re
from os.path import *

import mutagen
from mutagen.easyid3 import EasyID3 as easyid3

from Base import retrieveTags
from Base import tools
from Modules import albumArt
from Modules import albumName
from Modules import artistName
from Modules import composerName
from Modules import dateLenOrg
from Modules import songName
from Modules import songTitle


def inputSongDir(test=0):
    while True:
        if test:
            songDir = r'/home/hritwik/Videos/CR'
        else:
            songDir = input("Enter song dir:  ")

        if isdir(songDir):
            print("Song dir is: ", songDir)
            return songDir
        else:
            print("No such Dir exist, Please enter Dir again...")


# todo : add m4a support
def getSongList(files):
    songs = []
    for x in files:
        x = re.findall(r'(.+\.mp3)', x)
        if len(x) != 0:
            songs.append(x[0])
    return songs


def fixSongName(songDir, song_list, log_file, test=0):
    print("Fixing song names....")

    for song in song_list:
        try:
            songName.start(songDir, song, song_list)
        except:
            print("==================== There Was some error fixing name. Moving to next ====================")
            tools.writePrintLog(log_file,
                                '\n\n==================== Error fixing name: ' + song + ' ====================\n',
                                test=test)
    print()


# todo : add m4a support
def fixTags(song_dir, song_list, log_file, get_from_web_flag=0, test=0):
    for song in song_list:
        song_with_path = os.path.join(song_dir, song)

        try:
            tags = easyid3(song_with_path)
        except:
            print(" ==================== This Song has no tags. Creating tags... ==================== ")
            try:
                tags = mutagen.File(song_with_path, easy=True)
                tags.add_tags()
                print("Tags created.")
            except:
                print("==================== There Was some error creating tags. Moving to next ====================")
                tools.writePrintLog(log_file,
                                    '\n\n==================== Error creating tags: ' + song_with_path + ' ====================\n',
                                    test=test)

                continue

        # song_name = tools.removeBitrate(song)
        # song_name = song_name.replace('.mp3', '')
        song_name = song.replace('.mp3', '').strip()

        print("Song Name: ", song_name)

        if get_from_web_flag:
            try:
                json_data = retrieveTags.start(tags, song_name, log_file, song_with_path, test=test)

                # None can only be returned in case of any error, so we were not able to find data
                if json_data is not None:
                    found_data = 1
                else:
                    print(" ==================== No data found for this song... ==================== ")
                    found_data = 0
                    json_data = ''

                    log_file.write(
                        '\n\n ==================== Error: No data found for: ' + song_with_path + ' ==================== \n')
                    log_file.write("\nalbum={} \nartist={} \nYear={}".format(tags.get('album'), tags.get('artist'),
                                                                             tags.get('date')))
                    tools.writePrintLog(log_file, "\nerror=", test=test)

            except:
                found_data = 0
                json_data = ''
                print(" ==================== No data found for this song... ==================== ")

                log_file.write(
                    '\n\n ==================== Error: No data found for: ' + song_with_path + ' ==================== \n')
                log_file.write("\nalbum={} \nartist={} \nYear={}".format(tags.get('album'), tags.get('artist'),
                                                                         tags.get('date')))
                tools.writePrintLog(log_file, "\nerror=", test=test)


        else:
            found_data = 0
            json_data = ''

        print(found_data)
        input("HUEUH")

        try:
            albumName.start(tags, json_data, found_data)
        except:
            print("\n==================== There Was some error fixing albumName.==================== \n"
                  "Make sure year is there in song tags. if not, add it manually and re-run this program.\n"
                  "Moving to next tag...\n")

            tools.writePrintLog(log_file,
                                '\n\n ==================== Error in fixing album_name, song_with_path: ' + song_with_path + '====================\n',
                                test=test)

        try:
            artistName.start(tags, json_data, found_data)
        except:
            print(
                "\n==================== There Was some error fixing artistName. Moving to next ====================\n")

            tools.writePrintLog(log_file,
                                '\n\n==================== Error in artist_name: song_with_path: ' + song_with_path + ' ==================== \n',
                                test=test)

        try:
            composerName.start(tags, json_data, found_data)
        except:
            print(
                "\n==================== There Was some error fixing composerName. Moving to next ==================== \n")

            tools.writePrintLog(log_file,
                                '\n\n ==================== Error in composer: song_with_path:' + song_with_path + ' ==================== \n',
                                test=test)

        try:
            songTitle.start(tags, json_data, found_data)
        except:
            print(
                "\n ==================== There Was some error fixing songTitle. Moving to next ==================== \n")

            tools.writePrintLog(log_file,
                                '\n\n ==================== Error in title\n song_with_path: ' + song_with_path + ' ==================== \n',
                                test=test)

        try:
            dateLenOrg.start(tags, json_data, found_data)
        except:
            print(
                "\n ==================== There Was some error fixing Date, Len, Org. Moving to next ==================== \n")

            tools.writePrintLog(log_file,
                                '\n\n ==================== Error in date\n song_with_path =' + song_with_path + ' ==================== \n',
                                test=test)

        try:
            albumArt.start(json_data, song_dir, song_with_path, found_data)
        except:
            print(
                "\n ==================== There Was some error fixing albumArt. Moving to next ==================== \n")

            tools.writePrintLog(log_file,
                                '\n\n ==================== error in albumART\n song_with_path =' + song_with_path + ' ==================== \n',
                                test=test)

        print()


def handleSongs(song_dir, files, get_from_web_flag, sub_dir_flag=-1, test=0):
    print('Now in ', song_dir)

    if sub_dir_flag == 0 and int(input("Do you Want to Fix songs in " + song_dir + " ?\n1 == Yes, 0 == NO\n")) == 0:
        return

    log_file = tools.createLogFile(song_dir)
    song_list = getSongList(files)

    fixSongName(song_dir, song_list, log_file, test=test)
    fixTags(song_dir, song_list, log_file, get_from_web_flag, test=test)


def start(test=0):
    song_dir = inputSongDir(test)

    if test:
        sub_dir_flag = -1
        get_from_web_flag = 1
    else:
        sub_dir_flag = int(input("\nDo you want to run this program in all sub-dirs?\n"
                                 "1 == Yes,\n-1 == No,\n0 == Ask in each Dir\n"))
        get_from_web_flag = int(input('Do you want to retrieve missing tags from web? 0 == NO, 1 == YES'))

    if sub_dir_flag == -1:
        print("Only changing attributes in:", song_dir + "...\n")

        files = [
            x
            for x in os.listdir(song_dir)
            if isfile(os.path.join(song_dir, x))
        ]

        handleSongs(song_dir, files, get_from_web_flag, test=test)

    else:
        print("Walking down ", song_dir, "\b...")
        for curr_dir, sub_dirs, files in os.walk(song_dir, topdown=True):
            handleSongs(curr_dir, files, get_from_web_flag, sub_dir_flag, test=test)
