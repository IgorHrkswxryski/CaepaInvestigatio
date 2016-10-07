""" entry points """
import argparse

from caepainvestigatio import connect
from caepainvestigatio import onionrunner
from caepainvestigatio import linkJSONtoDB
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def run_onionscan(args=None):
    """ run scan onion """

    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Initial list onions")

    args = parser.parse_args(args)

    # TEST DEBUGGING
    log.debug("start onionrunner")

    connect.connectionToDB()
    onionrunner.onionrunner(args.path)

def SendJSONToDB(args=None):
    """ sens json to db """

    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Directory of JSON collecting files")

    args = parser.parse_args(args)

    log.debug("send JSON file to DB")

    connect.connectionToDB()

    linkJSONtoDB.JSONtoDB(args.path)

