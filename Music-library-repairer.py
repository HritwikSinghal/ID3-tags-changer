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

print("Enter number(s) corresponding to tag(s) you want to fix in songs")
print("If you want to fix multiple tags, have space b/w numbers (like '1 3 4')")
i = 1
for ele in list_of_tags:
    print('\t', i, '-', ele)
    i += 1
print('\t', 8, '-', 'All above')
change_tags = input().split()
print("Your input is", change_tags)

ret_web = int(input("If there is tag missing, do you want to retrieve it from web?"
                    "\n1 == YES, 0 == NO\n"))


# main.start(test=1)
