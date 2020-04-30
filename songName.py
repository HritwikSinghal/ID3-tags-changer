import os, re


def remove_bitrate(full_path_of_songs):
    i = -1
    # remove [320 kbps] from name
    for song in full_path_of_songs:
        i += 1
        x = re.findall(r'(.+) \[.*\](.mp3)', song)
        if len(x) != 0:
            new = ''.join(x[0])
            os.rename(song, new)
            full_path_of_songs[i] = new
    return full_path_of_songs


def start(full_path_of_songs):
    full_path_of_songs = remove_bitrate(full_path_of_songs)
