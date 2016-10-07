""" entry points """
import argparse

from caepainvestigatio import connect
from caepainvestigatio import onionrunner

def run_onionscan(args=None):
    """ run scan onion """

    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        help="Initial list onions")

    args = parser.parse_args(args)

    connect.connectionToDB()
    onionrunner.onionrunner(args.path)

