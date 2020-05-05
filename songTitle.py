import re
import tools


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
    tools.addIfTagMissing(tags, 'title', song_name, song_info)
    modifyTitle(tags)
