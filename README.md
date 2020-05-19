# Music-library-repairer

This program is in early stages so it may mess up a little bit
Please make a backup of your songs somewhere in case anything goes wrong.

I WILL NOT BE RESPONSIBLE FOR ANY MESS.

This program will fix the following tags for each song in your Music library

 - Album
 - Artist
 - Composer
 - Title
 - Date, Length (tag) & Label
 - AlbumArt
 - Song Name

if a song does not have these tags, it will download tags from saavn and append them to the song.
(It will ask if you want to retrieve data from web, just enter no to fix songs locally)

if 'retrieve from web' option is selected, it will try to automatch the song online with the tags in song on your drive. If it fails, it will ask you to select song.

If tags were not downloaded, these things will be fixed:
 - remove 'songs.pk' or 'djmaza.XXX' from song name and title and album
 - sorting of artists and remove duplicates
 - remove bitarte from song name if exists
	- remove '&quot' and ' - single' and '&amp' from tags
 - and many more..

Note: This library uses song name as param to search on web, so make sure the song name is 
      as accurate as possible for max accuracy.

Installation:

Clone this repository using
```sh
$ git clone https://github.com/HritwikSinghal/Music-library-repairer
```
Enter the directory and install all the requirements using
```sh
$ pip3 install -r requirements.txt
```
Run the app using
```sh
$ python3 Music-library-repairer.py
```

I have not tested this on linux, but there may be issue with file paths in any linux distro. if you find any issue, please open an issue on github. I will try to fix it 


**SS:** 
https://imgur.com/a/vDMHkqP
