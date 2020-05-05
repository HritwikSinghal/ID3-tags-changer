from Base import tools


def addDate(tags, song_name, song_info):
    if tools.isTagPresent(tags, 'date'):
        print("Curr Year: ", tags['date'][0])
        old_date = tags['date'][0]

        new_date = song_info['date']

        if old_date != new_date:
            tags['date'] = new_date
            tags.save()
            print("Added new date='" + new_date + "' to '" + song_name + "'")
    else:
        new_date = song_info['date']

        tags['date'] = new_date
        tags.save()
        print("Added new date='" + new_date + "' to '" + song_name + "'")


def addLen(tags, song_name, song_info):
    if tools.isTagPresent(tags, 'length'):
        print("Curr Length Value: ", tags['length'][0])

        old_len = tags['length'][0]
        new_len = song_info['length']

        if old_len != new_len:
            tags['length'] = new_len
            tags.save()
            print("Added new length='" + new_len + "' value to '" + song_name + "'")

    else:
        new_len = song_info['length']

        tags['length'] = new_len
        tags.save()
        print("Added new length='" + new_len + "' value to '" + song_name + "'")


def addOrg(tags, song_name, song_info):
    if tools.isTagPresent(tags, 'organization'):
        print("Curr  Label: ", tags['organization'][0])

        old_org = tags['organization'][0]
        new_org = song_info['organization']

        if old_org != new_org:
            tags['organization'] = new_org
            tags.save()
            print("Added new Label='" + new_org + "' value to '" + song_name + "'")
    else:
        new_org = song_info['organization']

        tags['organization'] = new_org
        tags.save()
        print("Added new Label='" + new_org + "' value to '" + song_name + "'")


def start(tags, song_name, song_info):
    addDate(tags, song_name, song_info)
    addLen(tags, song_name, song_info)
    addOrg(tags, song_name, song_info)
