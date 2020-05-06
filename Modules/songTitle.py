from Base import tools


def modifyTitle(tags):
    print("Curr Title: ", tags['title'][0])

    oldTitle = tags['title'][0]
    newTitle = tools.removeSiteName(oldTitle)
    newTitle = tools.removeGibberish(newTitle)

    if oldTitle != newTitle:
        tags['title'] = newTitle
        tags.save()
        print("New Title : ", newTitle)


def start(tags, song_name, song_info):
    title_value = song_info['title']
    tools.addIfTagMissing(tags, 'title', song_name, title_value)
    modifyTitle(tags)
