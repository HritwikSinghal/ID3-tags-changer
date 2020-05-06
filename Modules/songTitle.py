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


def start(tags, json_data, ask_flag=0):
    title_value = json_data['title']
    tools.checkAndFixTag(tags, 'title', title_value, ask_flag)

    modifyTitle(tags)
