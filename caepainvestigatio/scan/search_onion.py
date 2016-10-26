""" try to find onion link in snapshot """
import re

from caepainvestigatio.logging_conf import initLogging
from caepainvestigatio.ORM.categories import Category

log = initLogging()

def search_onion(onion_info):
    """ search onion in snapshot """

    links = []
    regex = ur"((?:[a-z0-9]+\.)*[a-z0-9]{16}.onion)"
    code = onion_info.snapshot

    finds = re.findall(regex, code)
    if finds != []:
        for elem in finds:
            if elem not in links and elem != onion_info.hiddenService:
                links.append(elem)

    log.debug("Links find to %s", links)
    return links
