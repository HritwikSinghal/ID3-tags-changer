from Base import tools


def fixComposer(tags):
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


def start(tags, json_data, ask_flag=0):
    composer_name = json_data['composer']
    tools.checkAndFixTag(tags, 'composer', composer_name, ask_flag)
    fixComposer(tags)
