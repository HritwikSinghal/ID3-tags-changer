import json

from mutagen.mp3 import MP3

from Base import jioSaavnApi
from Base import tools


def mod(num):
    if num >= 0:
        return num
    return -num


def autoMatch(song_info_list, song_name, tags, song_with_path, test=0):
    for song in song_info_list:
        json_data = json.loads(json.dumps(song))

        #################################################
        if test:
            # print(json.dumps(json_data, indent=4))
            print()
            print(json_data['title'].lower().strip())
            print(song_name.lower().strip())
        #################################################

        song_name = song_name.lower().strip()
        title = json_data['title'].lower().strip()

        ed_title = tools.editDistDP(song_name, title, len(song_name), len(title))
        if test:
            print(ed_title)

        if ed_title > 5:
            continue

        if tools.isTagPresent(tags, 'album'):

            album_from_tags = tools.removeYear(tags['album'][0]).lower().strip()
            # try:
            #     album_from_json = json_data['actual_album'].lower().strip()
            # except KeyError:
            album_from_json = json_data['album'].lower().strip()
            ed_album = tools.editDistDP(album_from_tags, album_from_json, len(album_from_tags), len(album_from_json))

            if test:
                print(album_from_json)
                print(album_from_tags)
                print(ed_album)

            if ed_album > 4:
                continue

        if tools.isTagPresent(tags, 'artist'):
            artist_from_json = json_data['singers']
            artist_from_json = tools.divideBySColon(artist_from_json)
            artist_from_json = tools.removeTrailingExtras(artist_from_json)
            artist_from_json = tools.removeDup(artist_from_json)

            artist_from_tags = tags['artist'][0]
            artist_from_tags = tools.divideBySColon(artist_from_tags)
            artist_from_tags = tools.removeTrailingExtras(artist_from_tags)
            artist_from_tags = tools.removeDup(artist_from_tags)

            ed_artist = tools.editDistDP(artist_from_tags, artist_from_json, len(artist_from_tags), len(artist_from_json))

            if test:
                print(artist_from_json)
                print(artist_from_tags)
                print(ed_artist)

            if ed_artist >= 11:
                continue

        audio = MP3(song_with_path)
        length_from_tags = int(audio.info.length)
        length_from_json = int(json_data['duration'])

        if test:
            print(length_from_json)
            print(length_from_tags)
            print(mod(length_from_json) - length_from_tags)

        if mod(length_from_json - length_from_tags) > 10:
            continue

        return song

    return None


def getSong(song_info_list, song_name, tags, song_with_path, test=0):
    # auto-match song
    song = autoMatch(song_info_list, song_name, tags, song_with_path, test)
    if song is not None:
        return song

    #############################
    # print("STOP")
    # x = input()
    #############################
    print("\n-------------------------------"
          "--------------------------------")
    print("-------------------------------"
          "--------------------------------\n")

    print("Your song info...")
    print('Name  : ', song_name)
    for key in tags.keys():
        print(key, ":", tags[key][0])

    # if no song was matched, Ask user

    print("\n-------------------------------"
          "\nDownloaded songs info, select song number to download.")

    # printing the song list
    i = 0
    for song in song_info_list:
        print(i + 1, end=' ) \n')
        for key in song:
            # if(key == )
            print('\t', key, ':', song[key])
        print()
        i += 1

    # now asking user
    song_number = input("\nEnter your song number from above list, if none matches, enter 'n': ")

    try:
        # if user entered 'n' or any letter, then conversion to int will fail and ValueError is raised

        # check if the user entered an index number which was out of range of list, if yes, ask user again
        if int(song_number) > len(song_info_list):
            song_number = int(input("\nOops..You mistyped, \n"
                                    "Please enter number within above range. If none matches, enter 'n': ")) - 1

            if song_number > len(song_info_list):
                return -1

    # if user entered 'n' or any letter, return -1 (since no song was matched correctly)
    except ValueError:
        return None

    song_number = int(song_number)
    return song_info_list[song_number - 1]


def start(tags, song_name, log_file, song_with_path, test=0):
    list_of_songs = jioSaavnApi.start(song_name, tags, log_file, test=test)

    song_info = getSong(list_of_songs, song_name, tags, song_with_path, test=test)

    if song_info is None:
        list_of_songs = jioSaavnApi.start(song_name, tags, log_file, retry_flag=1, test=test)
        song_info = getSong(list_of_songs, song_name, tags, song_with_path, test=test)

    return song_info
