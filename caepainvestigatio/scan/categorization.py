""" try to categorize the onion """
from caepainvestigatio.logging_conf import initLogging
from caepainvestigatio.ORM.categories import Category
from caepainvestigatio import connect
from langdetect import detect

log = initLogging()

def language(onion_info):
    """ search to categorize the onion """

    if onion_info.snapshot == "" or onion_info.snapshot is None:
        return None

    lang = detect(onion_info.snapshot)
    return lang

def search_category(onion_info):
    """ try to categorize with dictionnary a website """

    category_find = []
    for category in Category.objects():
        for expression in category.expressions:
            # find expression in onion website sources
            if expression in onion_info.snapshot:
                log.debug("detect category %s for onion %s" % (category.category, onion_info.hiddenService))
                if category not in category_find:
                    category_find.append(category)

    return category_find
