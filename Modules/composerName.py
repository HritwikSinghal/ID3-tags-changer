from Base import tools


def fixComposer(tags):
    if tools.isTagPresent(tags, 'composer'):
        old_composer = tags['composer'][0]
        print("Composer: ", old_composer)

        new_composer = tools.removeGibberish(old_composer)
        new_composer = tools.divideBySColon(new_composer)

        new_composer = tools.removeTrailingExtras(new_composer)
        new_composer = tools.removeDup(new_composer)

        if new_composer != old_composer:
            tags['composer'] = new_composer
            tags.save()
            print("New Composer: ", new_composer)
    else:
        print("No composer found and No data was retrieved from web")


def start(tags, json_data, found_data):
    if found_data:
        composer_name = json_data['composer']
        tools.checkAndFixTag(tags, 'composer', composer_name)

    fixComposer(tags)
