import os

from Base import main


def start(test=0):
	if test:
		main.start(1)
	else:
		list_of_tags = [
			'Album',
			'Artist',
			'Composer',
			'Title',
			'Date, Length(tag) & Label',
			'AlbumArt',
			'Song Name'
		]

		print("""
            |  \/  |         (_)      | |   (_) |                          | ___ \               (_)              
            | .  . |_   _ ___ _  ___  | |    _| |__  _ __ __ _ _ __ _   _  | |_/ /___ _ __   __ _ _ _ __ ___ _ __ 
            | |\/| | | | / __| |/ __| | |   | | '_ \| '__/ _` | '__| | | | |    // _ \ '_ \ / _` | | '__/ _ \ '__|
            | |  | | |_| \__ \ | (__  | |___| | |_) | | | (_| | |  | |_| | | |\ \  __/ |_) | (_| | | | |  __/ |   
            \_|  |_/\__,_|___/_|\___| \_____/_|_.__/|_|  \__,_|_|   \__, | \_| \_\___| .__/ \__,_|_|_|  \___|_|   
                                                                     __/ |           | |                          
                                                                    |___/            |_|                      
        """)

		print("""
            This program will fix the following tags for each song in your Music library
            For more info, visit https://github.com/HritwikSinghal/Music-library-repairer
        """)

		i = 0
		for ele in list_of_tags:
			print('\t', i + 1, '-', ele)
			i += 1

		print('''
            Warning: This program is in early stages so it may mess up a little bit
                    Please make a backup of your songs somewhere in case anything goes wrong.
                    I WILL NOT BE RESPONSIBLE FOR ANY MESS.
                    Enter 'yes' TO RUN OR 'no' TO EXIT (IN LOWER CASE)
        ''')

		x = input()

		if x == 'yes':
			print("Starting Program....")
			main.start(test)

			print("""
                    If there were errors during running this program, please upload log file
                    named 'Music-library-repairer_LOGS.txt' in each dir and open an issue on github
                    you can find those log files by using default search in folders or by manually
                    finding each.
                """)
			print('''
                    Thank you for Using this program....
                    By Hritwik
                    https://github.com/HritwikSinghal
                ''')
		else:
			print("Exiting....")
			exit(0)


if os.path.isfile(os.path.join("Base", "test_bit.py")):
	test = 1
else:
	test = 0

start(test=test)

# todo : add m4a support
# todo: rename song name as song title after retrieving it from web
# todo: take better logs
# todo:- get songs from multiple pages or api's
#       maybe change to spitify api or gaana (if songs are not available on spotify)
#       or make it search from all 3
