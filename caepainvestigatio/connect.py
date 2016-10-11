""" DB connection function """
from mongoengine import connect
from caepainvestigatio.logging_conf import initLogging

log = initLogging()

def connectionToDB():
    """ Connect to mongoDB database """

    connection = connect('TORUser')
    if connection is None:
        log.error("No connection to DB")
    return connection
