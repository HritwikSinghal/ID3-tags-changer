from Base import tools


def addDate(tags):
    print("Curr Title: ", tags['title'][0])

    oldTitle = tags['title'][0]
    newTitle = tools.removeSiteName(oldTitle)
    newTitle = tools.removeGibberish(newTitle)

    if oldTitle != newTitle:
        tags['title'] = newTitle
        # tags.save()
        print("New Title : ", newTitle)


def addLen(tags):
    print("Curr Title: ", tags['title'][0])

    oldTitle = tags['title'][0]
    newTitle = tools.removeSiteName(oldTitle)
    newTitle = tools.removeGibberish(newTitle)

    if oldTitle != newTitle:
        tags['title'] = newTitle
        # tags.save()
        print("New Title : ", newTitle)


def addOrg(tags):
    print("Curr Title: ", tags['title'][0])

    oldTitle = tags['title'][0]
    newTitle = tools.removeSiteName(oldTitle)
    newTitle = tools.removeGibberish(newTitle)

    if oldTitle != newTitle:
        tags['title'] = newTitle
        # tags.save()
        print("New Title : ", newTitle)


def start(tags, song_name, song_info):
    tools.addIfTagMissing(tags, 'len', song_name, song_info)
    tools.addIfTagMissing(tags, 'organization', song_name, song_info)
    tools.addIfTagMissing(tags, 'date', song_name, song_info)

    addOrg(tags)
    addDate(tags)
    addLen(tags)
