""" try to find information from onion ip on shodan or cymon """

import time
from datetime import datetime
from cymon import Cymon
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def shodan_search(onion_info, shodan_client):
    """ search information in shodan """

    if shodan_client is None:
        log.error("Shodan not connected")
        return None

    if onion_info is None:
        log.error("No onion send in shodan_search")
        return None

    result_ip = ip_search(onion_info.ipAddresses, shodan_client)
    result_ssh = ssh_search(onion_info.sshKey, shodan_client)
    return [result_ip, result_ssh]

def ip_search(ip_addresses, shodan_client):
    """ Try to find ip in onion """

    shodan_result = {}

    if ip_addresses is not None and ip_addresses != []:
        for ip in ip_addresses:
            result = None

            try:
                result = shodan_client.search(ip)
            except:
                log.warning("Can't search %s on shodan", ip)
                pass

            if result['total'] > 0:
                log.debug("find %s on shodan", ip)
                shodan_result[ip] = result

    return shodan_result

def ssh_search(sshkey, shodan_client):
    """ Try to find ssh key in onion info """

    if sshkey is not None:
        result = None

        try:
            result = shodan_client.search(sshkey)
        except:
            log.warning("Can't search %s on shodan", sshkey)
            return None

        if result['total'] > 0:
            log.debug("find %s on shodan", sshkey)
            return result

    return None
