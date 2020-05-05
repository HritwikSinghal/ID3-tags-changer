from Base import tools


def modifyComposer(tags):
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


def start(tags, song_name, song_info):
    tools.addIfTagMissing(tags, 'composer', song_name, song_info)
    modifyComposer(tags)
