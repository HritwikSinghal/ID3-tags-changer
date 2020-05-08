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
        """)

        i = 0
        for ele in list_of_tags:
            print('\t', i + 1, '-', ele)
            i += 1

        print('''
            Warning: This program is in early stages so it may mess up a little bit
                    Please make a backup of your songs somewhere in case anything goes wrong.
                    I WILL NOT BE RESPONSIBLE FOR ANY MESS.
                    PLEASE ENTER '1' TO CONFIRM RUNNING THIS PROGRAM OR '0' TO EXIT
        ''')

        x = int(input())

        if x == 0:
            print("Exiting....")
            exit(0)

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


os.chdir(os.getcwd())
if os.path.isfile(os.path.join("Base", "test_bit.py")):
    test_bit = 1
else:
    test_bit = 0

print(test_bit)
start(test=test_bit)

# todo:
''' 
-change the asking logic to : if more than one song is found
    with same album
-code cleanup
-make more verbose logs

- the part after ("fromxxx") is correct album name
-improve song recognization
-it recognized wrong album name for dilbara since it was released as single
    its saavn api fault, maybe change to spitify api
    or gaana (if songs are not available on spotify)
    or make it search from all 3

'''