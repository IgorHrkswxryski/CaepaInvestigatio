""" try to categorize the onion """
import re

from caepainvestigatio.logging_conf import initLogging
from caepainvestigatio.ORM.categories import Category
from langdetect import detect

log = initLogging()

def language(onion_info):
    """ search to categorize the onion """

    if onion_info.snapshot == "" or onion_info.snapshot is None:
        return None

    try:
        lang = detect(onion_info.snapshot)
    except:
        log.warning("Can't determine lang")
        return None

    log.info("lang detected : %s", lang)
    return lang

def search_category(onion_info):
    """ try to categorize with dictionnary a website """

    category_find = []
    for category in Category.objects():
        count_w = 0
        for expression in category.expressions:
            # find expression in onion website sources
            count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(expression), onion_info.snapshot))
            if count > 0:
                count_w += count
                if count_w > 2 and category not in category_find:
                    log.debug("detect category %s for onion %s", category.category, onion_info.hiddenService)
                    category_find.append(category)
                    break

    return category_find
