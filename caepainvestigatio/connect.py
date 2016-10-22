""" DB connection function """
from mongoengine import connect
from os import environ
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def connectionToDB():
    """ Connect to mongoDB database """

    connection = connect('TORUser', host=environ.get('MONGO_URL'))
    if connection is None:
        log.error("No connection to DB")
    return connection
