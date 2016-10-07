from mongoengine import connect
from logging_conf import initLogging

def connectionToDB():
    """ Connect to mongoDB database """
    connection = connect('TORUser')
    # TEST DEBUGGING
    initLogging().debug(connection)
    return connection

connectionToDB()

