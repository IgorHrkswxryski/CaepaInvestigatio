""" entry points """
import argparse

from caepainvestigatio import connect
from caepainvestigatio import onionrunner
from caepainvestigatio import linkJSONtoDB
from caepainvestigatio import scan_onions
from caepainvestigatio.ORM.categories import feed_db


def run_onionscan(args=None):
    """ run scan onion """

    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Initial list onions")

    args = parser.parse_args(args)

    connect.connectionToDB()
    onionrunner.onionrunner(args.path)

def send_json_to_db(args=None):
    """ sens json to db """

    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Directory of JSON collecting files")

    args = parser.parse_args(args)

    connect.connectionToDB()

    linkJSONtoDB.JSONtoDB(args.path)

def run_scan_onions(args=None):
    """ scan onions data and send result to database """

    parser = argparse.ArgumentParser()
    parser.add_argument("client_shodan",
                        help="client shodan pass")

    args = parser.parse_args(args)

    connect.connectionToDB()

    scan_onions.scan(args.client_shodan)

def feed_category_db(args=None):
    """ feed category collection for analyses """

    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="path of file containing words")

    args = parser.parse_args(args)

    connect.connectionToDB()

    feed_db(args.path)
