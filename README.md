# Music-library-repairer


This program will fix the following tags for each song in your Music library
   1 - Album
	 2 - Artist
	 3 - Composer
	 4 - Title
	 5 - Date, Length(tag) & Label
	 6 - AlbumArt
	 7 - Song Name

if a song does not have these tags, it will download tags from saavn and append them to the song.
(It will ask if you want to retrieve data from web, just enter no to fix songs locally)

If tags were not downloaded, these things will be fixed:
 - remove 'songs.pk' or 'djmaza.XXX' from song name and title and album
 - sorting of artists and remove duplicates
 - remove bitarte from song name if exists
 - and many more..

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
