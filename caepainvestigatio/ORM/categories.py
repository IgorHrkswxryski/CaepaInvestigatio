""" ORM Category class """
import os
import re

import mongoengine

from caepainvestigatio.logging_conf import initLogging

log = initLogging()

class Category(mongoengine.Document):
    """ This class contain word per categry to categorize onions website """

    meta = {
        'indexes':[
            'category'
        ]
    }

    # name category
    category = mongoengine.StringField(Required=True, unique=True)

    # expressions in category
    expressions = mongoengine.ListField(mongoengine.StringField(unique=True))

def open_category_file(path_file):
    """ open category file """

    # open dico
    if os.path.exists(path_file):
        with open(path_file, "r") as dico:
            cat_list = dico.read().splitlines()
    else:
        log.error("No word list.")
        return None
    return cat_list

def add_category_to_db(category, words):
    """ save category on mongo """

    try:
        Category(category=category, expressions=words).save()
    except mongoengine.NotUniqueError:
        cat = Category.objects(category=category).first()
        cat.update(expressions=words)
        cat.save()


def feed_db(path_file):
    """ Read file and put all category in mongo db """

    cat_list = open_category_file(path_file)
    if not cat_list:
        return False

    category = None
    words = []
    for line in cat_list:
        if "category" in line:
            result = re.match("<category: (.+)>", line)
            if category:
                add_category_to_db(category, words)
            words = []
            if result is not None:
                category = result.group(1)
                log.debug("categorie: %s", category)
                continue

        if not line.strip():
            continue

        if category is None:
            log.error("Wrong file %s", path_file)
            return False

        words.append(line)

    return True
