from Modules import main

# todo: implement caching using e_songid

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
main.start(test=1)

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
