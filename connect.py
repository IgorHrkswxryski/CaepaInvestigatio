from mongoengine import connect

def connectionToDB():
    """ Connect to mongoDB database """

    connection = connect('TORUser', username='TORUser', password='coucou')
    print(connection)
