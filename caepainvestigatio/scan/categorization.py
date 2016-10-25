""" try to categorize the onion """

from caepainvestigatio.logging_conf import initLogging
from langdetect import detect

log = initLogging()

def language(onion_info):
    """ search to categorize the onion """

    if onion_info.snapshot == "" or onion_info.snapshot is None:
        return None

    lang = detect(onion_info.snapshot)
    return lang
