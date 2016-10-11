""" onionrunner """
import codecs
import json
import random
import subprocess
import time

from stem.control import Controller
from stem import Signal
from threading import Timer
from threading import Event
from caepainvestigatio import linkJSONtoDB
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

onions         = []
session_onions = []

identity_lock  = Event()
identity_lock.set()

def get_onion_list(path_list):
    """ Grab the list of onions from our master list file. """

    # open the master list
    if os.path.exists(path_list):
        with open(path_list, "rb") as filed:
            stored_onions = filed.read().splitlines()
    else:
        log.error("[!] No onion master list. Download it!")
        return None

    log.debug("[*] Total onions for scanning: %d" % len(stored_onions))

    return stored_onions

def store_onion(onion):
    """  Stores an onion in the master list of onions. """

    log.debug("[++] Storing %s in master list." % onion)

    with codecs.open("onion_master_list.txt", "ab", encoding="utf8") as filed:
        filed.write("%s\n" % onion)

    return

def run_onionscan(onion):
    """ Runs onion scan as a child process. """

    log.debug("[*] Onionscanning %s" % onion)

    # fire up onionscan
    process = subprocess.Popen(["onionscan", "--jsonReport", "--simpleReport=false", onion], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # start the timer and let it run 5 minutes
    process_timer = Timer(300, handle_timeout, args=[process, onion])
    process_timer.start()

    # wait for the onion scan results
    stdout = process.communicate()[0]

    # we have received valid results so we can kill the timer
    if process_timer.is_alive():
        process_timer.cancel()
        return stdout

    log.warning("[!!!] Process timed out!")

    return None

def handle_timeout(process,onion):
    """ Handle a timeout from the onionscan process. """

    # halt the main thread while we grab a new identity
    identity_lock.clear()

    # kill the onionscan process
    try:
        process.kill()
        log.debug("[!!!] Killed the onionscan process.")
    except:
        pass

    # Now we switch TOR identities to make sure we have a good connection
    with Controller.from_port(port=9051) as torcontrol:

        # authenticate to our local TOR controller
        torcontrol.authenticate("coucou")

        # send the signal for a new identity
        torcontrol.signal(Signal.NEWNYM)

        # wait for the new identity to be initialized
        time.sleep(torcontrol.get_newnym_wait())

        log.debug("[!!!] Switched TOR identities.")

    # push the onion back on to the list
    session_onions.append(onion)
    random.shuffle(session_onions)

    # allow the main thread to resume executing
    identity_lock.set()

    return

def process_results(onion, json_response):
    """ Processes the JSON result from onionscan. """

    # create our output folder if necessary
    if not os.path.exists("onionscan_results"):
        os.mkdir("onionscan_results")

    # write out the JSON results of the scan
    with open("%s/%s.json" % ("onionscan_results", onion), "wb") as filed:
        filed.write(json_response)

    # send output in database
    linkJSONtoDB.send_db(json_response)

    # look for additional .onion domains to add to our scan list
    scan_result = ur"%s" % json_response.decode("utf8")
    scan_result = json.loads(scan_result)

    if scan_result['linkedSites'] is not None:
        add_new_onions(scan_result['linkedSites'])

    if scan_result['relatedOnionDomains'] is not None:
        add_new_onions(scan_result['relatedOnionDomains'])

    if scan_result['relatedOnionServices'] is not None:
        add_new_onions(scan_result['relatedOnionServices'])

    return

def add_new_onions(new_onion_list):
    """ Handle new onions. """

    global onions
    global session_onions

    for linked_onion in new_onion_list:

        if linked_onion not in onions and linked_onion.endswith(".onion"):

            log.debug("[++] Discovered new .onion => %s" % linked_onion)

            onions.append(linked_onion)
            session_onions.append(linked_onion)
            random.shuffle(session_onions)
            store_onion(linked_onion)

    return

def onionrunner(path_list_onion):
    """ start onionrunner """

    global onions
    global session_onions


    # get a list of onions to process
    onions = get_onion_list(path_list_onion)
    if onions is None:
        return

    # randomize the list a bit
    random.shuffle(onions)
    session_onions = list(onions)

    count = 0

    while count < len(onions):

        # if the event is cleared we will halt here
        # otherwise we continue executing
        identity_lock.wait()

        # grab a new onion to scan
        log.debug("[*] Running %d of %d." % (count, len(onions)))
        onion = session_onions.pop()

        # test to see if we have already retrieved results for this onion
        if os.path.exists("onionscan_results/%s.json" % onion):
            log.debug("[!] Already retrieved %s. Skipping." % onion)
            count += 1
            continue

        # run the onion scan	
        result = run_onionscan(onion)

        # process the results
        if result is not None:
            if len(result):
                process_results(onion, result)

        count += 1
