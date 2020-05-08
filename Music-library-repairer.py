import os
from Modules import main


def start(test=0):
    # todo: implement caching using e_songid

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
                    PLEASE ENTER IN LOWER CASE 'yes' TO RUN OR 'no' TO EXIT
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


os.chdir(os.getcwd())
if os.path.isfile(os.path.join("Base", "test_bit.py")):
    test_bit = 1
else:
    test_bit = 0

start(test=test_bit)

# # todo: if user selects 'n', try searching with artist or year

''' 
-code cleanup
-make more verbose logs
- rename song name as song title after retrieving it from web

-get songs from multiple pages or api's
-it recognized wrong album name for dilbara since it was released as single
    its saavn api fault, maybe change to spitify api
    or gaana (if songs are not available on spotify)
    or make it search from all 3

'''
