""" ORM Analyse class """
import mongoengine
import datetime

class Result(mongoengine.EmbeddedDocument):
    """ This class contain all result of our analysis on an onion """

    meta = {
        'indexes' : [
            'onion'
        ]
    }

    # onion id
    onion = mongoengine.StringField(required=True)

    # check date
    date_check = mongoengine.DateTimeField(default=datetime.datetime.utcnow,
                                           required=True)

    # server ip
    server_ip = mongoengine.StringField()

    # shodan
    shodan_result = mongoengine.StringField()

    # cymon
    cymon_result = mongoengine.StringField()

    # lang
    lang = mongoengine.StringField()

    # category
    category = mongoengine.StringField()

