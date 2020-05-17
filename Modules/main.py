# This was a major help
# https://stackoverflow.com/questions/42231932/writing-id3-tags-using-easyid3

import os
import mutagen
from os.path import isfile, isdir
from mutagen.easyid3 import EasyID3 as easyid3
from Base import tools
import traceback

from Modules import addDateLenOrg
from Modules import albumArt
from Modules import albumName
from Modules import artistName
from Modules import composerName
from Modules import songName
from Base import retrieveTags
from Modules import songTitle


def inputSongDir(test=0):
    while True:
        if test == 1:
            songDir = r'C:\Users\hritwik\Pictures\Camera Roll'
        else:
            songDir = input("Enter song dir:  ")

        if isdir(songDir):
            print("Song dir is: ", songDir)
            return songDir
        else:
            print("No such Dir exist, Please enter Dir again...")


def getSongList(files):
    songs = []
    for x in files:
        x = tools.re.findall(r'(.+\.mp3)', x)
        if len(x) != 0:
            songs.append(x[0])
    return songs


def changeSongName(songDir, song_list, log_file, test=0):
    print("Fixing song names....")

    for song in song_list:
        try:
            songName.start(songDir, song, song_list)
        except:
            print("XXX---There Was some error fixing name. Moving to next")
            tools.writeAndPrintLog(log_file, '\n\nXXX---error fixing name== ' + song + '\n', test)
    print()


def fixTags(song_dir, song_list, log_file, get_from_web_flag, test=0):
    for song in song_list:
        song_with_path = tools.join(song_dir, song)

        try:
            tags = easyid3(song_with_path)
        except:
            print("This Song has no tags. Creating tags...")
            try:
                tags = mutagen.File(song_with_path, easy=True)
                tags.add_tags()
                print("Tags created.")
            except:
                print("XXX---There Was some error creating tags. Moving to next")
                tools.writeAndPrintLog(log_file, '\n\nXXX---error creating tags= ' + song_with_path + '\n', test)

                continue

        song_name = tools.removeBitrate(song)
        song_name = song_name.replace('.mp3', '')
        song_name = song_name.strip()
        print("Song Name: ", song_name)

        if get_from_web_flag:
            try:
                json_data = retrieveTags.start(tags, song_name, log_file, test=test)

                # None can only be returned in case of any error, so we were not able to find data
                if json_data is not None:
                    found_data = 1
                else:
                    print("No data found for this song...")
                    found_data = 0
                    json_data = ''

                    log_file.write('\n\nXXX---error: No data found for = ' + song_with_path + '\n')
                    log_file.write("\nalbum={} \nartist={} \nYear={}".format(tags.get('album'), tags.get('artist'),
                                                                             tags.get('date')))
                    tools.writeAndPrintLog(log_file, "\nerror=", test=test)

            except:
                found_data = 0
                json_data = ''
                print("No data found for this song...")

                log_file.write('\n\nXXX---error: No data found for = ' + song_with_path + '\n')
                log_file.write("\nalbum={} \nartist={} \nYear={}".format(tags.get('album'), tags.get('artist'),
                                                                         tags.get('date')))
                tools.writeAndPrintLog(log_file, "\nerror=", test=test)


        else:
            found_data = 0
            json_data = ''

        #
        #
        #

        # try:
        #     albumName.start(tags, json_data, found_data)
        # except:
        #     print("\nXXX---There Was some error fixing albumName.\n"
        #           "Make sure year is there in song tags. if not, add it manually and re-run this program.\n"
        #           "Moving to next tag...\n")
        #
        #     tools.writeAndPrintLog(log_file,
        #                            '\n\nXXX---error in fixing albumname\n song_with_path =' + song_with_path + '\n',
        #                            test)
        #
        # try:
        #     artistName.start(tags, json_data, found_data)
        # except:
        #     print("\nXXX---There Was some error fixing artistName. Moving to next\n")
        #
        #     tools.writeAndPrintLog(log_file,
        #                            '\n\nXXX---error in artistname \n song_with_path =' + song_with_path + '\n',
        #                            test)
        #
        # try:
        #     composerName.start(tags, json_data, found_data)
        # except:
        #     print("\nXXX---There Was some error fixing composerName. Moving to next\n")
        #
        #     tools.writeAndPrintLog(log_file, '\n\nXXX---error in composer\n song_with_path =' + song_with_path + '\n',
        #                            test)
        #
        # try:
        #     songTitle.start(tags, json_data, found_data)
        # except:
        #     print("\nXXX---There Was some error fixing songTitle. Moving to next\n")
        #
        #     tools.writeAndPrintLog(log_file, '\n\nXXX---error in title\n song_with_path =' + song_with_path + '\n',
        #                            test)
        #
        # try:
        #     addDateLenOrg.start(tags, json_data, found_data)
        # except:
        #     print("\nXXX---There Was some error fixing Date, Len, Org. Moving to next\n")
        #
        #     tools.writeAndPrintLog(log_file, '\n\nXXX---error in date\n song_with_path =' + song_with_path + '\n', test)
        #
        # try:
        #     albumArt.start(json_data, song_dir, song_with_path, found_data)
        # except:
        #     print("\nXXX---There Was some error fixing albumArt. Moving to next\n")
        #
        #     tools.writeAndPrintLog(log_file, '\n\nXXX---error in albumART\n song_with_path =' + song_with_path + '\n',
        #                            test)

        print()


def handleSongs(song_dir, files, get_from_web_flag, sub_dir_flag=1, test=0):
    print('Now in ', song_dir)

    if sub_dir_flag == 0 and int(input("Do you Want to Fix songs in " + song_dir + " ?\n1 == Yes, 0 == NO\n")) == 0:
        return

    log_file = tools.createLogFile(song_dir)
    song_list = getSongList(files)

    changeSongName(song_dir, song_list, log_file, test=test)
    fixTags(song_dir, song_list, log_file, get_from_web_flag, test=test)


def start(test=0):
    song_dir = inputSongDir(test)

    if test == 1:
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
            if isfile(tools.join(song_dir, x))
        ]

        handleSongs(song_dir, files, get_from_web_flag, test=test)

    else:
        print("Walking down ", song_dir, "\b...")
        for curr_dir, sub_dirs, files in tools.os.walk(song_dir, topdown=True):
            handleSongs(curr_dir, files, sub_dir_flag, get_from_web_flag, test=test)
