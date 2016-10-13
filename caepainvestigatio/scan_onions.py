""" browse each onion collected to scan it """
import mongoengine
import shodan

from caepainvestigatio.ORM import results
from caepainvestigatio.ORM import collect
from caepainvestigatio import connect
from caepainvestigatio.scan import shodan_analyses
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def scan(shodan_client_api_key):
    """ scan all onion collected """

    shodan_client = shodan.Shodan(shodan_client_api_key)

    for onion_info in collect.Collect.objects():
        shodan_results = shodan_analyses.shodan_search(onion_info, shodan_client)
        log.debug("find on shodan %s : %s", collect.hiddenService, shodan_results)

        try:
            results.result(onion=onion_info.hiddenService,
                           shodan_ip_result=shodan_results[0],
                           shodan_keyssh_result=shodan_results[1])
        except mongoengine.NotUniqueError:
            res = results.result.objects(onion=onion_info.hiddenService).first()
            res.shodan_ip_result = shodan_results[0]
            res.shodan_keyssh_result = shodan_results[1]
            res.save()
        except:
            log.error("Can't connect collection result\n")
