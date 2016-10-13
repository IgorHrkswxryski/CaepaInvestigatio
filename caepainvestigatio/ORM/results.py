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
    onion = mongoengine.StringField(required=True, unique=True)

    # check date
    date_check = mongoengine.DateTimeField(default=datetime.datetime.utcnow,
                                           required=True)

    # shodan
    shodan_ip_result = mongoengine.DictField()

    # shodan
    shodan_keyssh_result = mongoengine.StringField()

    # cymon
    cymon_ip_result = mongoengine.DictField()

    # lang
    lang = mongoengine.StringField()

    # category
    category = mongoengine.StringField()

