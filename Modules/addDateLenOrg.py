from Base import tools


def addDate(tags, json_data):
    if tools.isTagPresent(tags, 'date'):
        print("Curr Year: ", tags['date'][0])
        old_date = tags['date'][0]

        new_date = json_data['date']

        if old_date != new_date:
            tags['date'] = new_date
            tags.save()
            print("Added new date='" + new_date)
    else:
        new_date = json_data['date']

        tags['date'] = new_date
        tags.save()
        print("Added new date='" + new_date)


def addLen(tags, json_data):
    if tools.isTagPresent(tags, 'length'):
        print("Curr Length Value: ", tags['length'][0])

        old_len = tags['length'][0]
        new_len = json_data['length']

        if old_len != new_len:
            tags['length'] = new_len
            tags.save()
            print("Added new length='" + new_len)

    else:
        new_len = json_data['length']

        tags['length'] = new_len
        tags.save()
        print("Added new length='" + new_len)


def addOrg(tags, json_data):
    if tools.isTagPresent(tags, 'organization'):
        print("Curr  Label: ", tags['organization'][0])

        old_org = tags['organization'][0]
        new_org = json_data['organization']

        if old_org != new_org:
            tags['organization'] = new_org
            tags.save()
            print("Added new Label='" + new_org)
    else:
        new_org = json_data['organization']

        tags['organization'] = new_org
        tags.save()
        print("Added new Label='" + new_org)


def start(tags, json_data):
    addDate(tags, json_data)
    addLen(tags, json_data)
    addOrg(tags, json_data)
