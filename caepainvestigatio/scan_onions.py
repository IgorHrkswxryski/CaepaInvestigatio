""" browse each onion collected to scan it """
import mongoengine
import shodan

from caepainvestigatio.ORM import results
from caepainvestigatio.ORM import collect
from caepainvestigatio import connect
from caepainvestigatio.scan import shodan_analyses, categorization
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def scan(shodan_client_api_key):
    """ scan all onion collected """

    shodan_client = shodan.Shodan(shodan_client_api_key)

    for onion_info in collect.Collect.objects():
        log.debug("scan onion %s", onion_info.hiddenService)
        shodan_results = shodan_analyses.shodan_search(onion_info, shodan_client)
        log.info("find on shodan %s : %s", onion_info.hiddenService, shodan_results)
        lang = categorization.language(onion_info)
        log.info("lang detected : %s", lang)
        category = categorization.search_category(onion_info)

        try:
            res = results.Result()
            res.onion = onion_info.hiddenService
            res.shodan_ip_result = shodan_results[0]
            res.shodan_keyssh_result = shodan_results[1]
            res.lang = lang
            res.save()
        except mongoengine.NotUniqueError:
            res = results.Result.objects(onion=onion_info.hiddenService).first()
            res.shodan_ip_result = shodan_results[0]
            res.shodan_keyssh_result = shodan_results[1]
            res.lang = lang
            res.save()
        except:
            log.error("Can't connect collection Result")
