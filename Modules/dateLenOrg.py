from Base import tools


def addDate(tags, json_data):
    if tools.isTagPresent(tags, 'date'):
        print("Curr Year: ", tags['date'][0])
        old_date = tags['date'][0]

        new_date = json_data['year']
        if old_date != new_date:
            tools.saveTags('date', new_date, tags)

    else:
        new_date = json_data['year']
        tools.saveTags('date', new_date, tags)


def addLen(tags, json_data):
    if tools.isTagPresent(tags, 'length'):
        print("Curr Length Value: ", tags['length'][0])

        old_len = tags['length'][0]
        new_len = json_data['duration']

        if old_len != new_len:
            tools.saveTags('length', new_len, tags)

    else:
        new_len = json_data['duration']
        tools.saveTags('length', new_len, tags)


def addOrg(tags, json_data):
    if tools.isTagPresent(tags, 'organization'):
        print("Curr  Label: ", tags['organization'][0])

        old_org = tags['organization'][0]
        new_org = json_data['label']

        if old_org != new_org:
            tools.saveTags('organization', new_org, tags)

    else:
        new_org = json_data['label']
        tools.saveTags('organization', new_org, tags)


def start(tags, json_data, found_data):
    if found_data:
        addDate(tags, json_data)
        addLen(tags, json_data)
        addOrg(tags, json_data)
