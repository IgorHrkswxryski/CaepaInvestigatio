from mongoengine import connect

def connectionToDB():
    """ Connect to mongoDB database """

    connection = connect('TORUser')
    print(connection)
