""" ORM Collect class """
import mongoengine
import datetime
import json
import bson

class Collect(mongoengine.Document):
    """ This class contain all onions of our TOR scan """

    meta = {
        'indexes':[
            'hiddenService'
        ]
    }

    # onion id
    #id = mongoengine.StringField(primary_key=True, default=(lambda : str(bson.ObjectId())))

    # check date
    date_check = mongoengine.DateTimeField(default=datetime.datetime.utcnow,
                                           required=True)

    # dateScanned
    dateScanned = mongoengine.StringField()

    # hidden service name
    hiddenService = mongoengine.StringField(required=True, unique=True)

    # online
    online = mongoengine.BooleanField()

    # performed scans
    performedScans = mongoengine.ListField()

    # WEB service detected
    webDetected = mongoengine.BooleanField()

    # TLS ciphering detected
    tlsDetected = mongoengine.BooleanField()

    # server SSH detected
    sshDetected = mongoengine.BooleanField()

    # server ricochet detected
    ricochetDetected = mongoengine.BooleanField()

    # server IRC detected
    ircDetected = mongoengine.BooleanField()

    # server FTP detected
    ftpDetected = mongoengine.BooleanField()

    # server smtp detected
    smtpDetected = mongoengine.BooleanField()

    # Bitcoin node detected
    bitcoinDetected = mongoengine.BooleanField()

    # server mongodb detected
    mongodbDetected = mongoengine.BooleanField()

    # server VNC detected
    vncDetected = mongoengine.BooleanField()

    # server xmpp detected
    xmppDetected = mongoengine.BooleanField()

    # detect skynet   
    skynetDetected = mongoengine.BooleanField()

    # crawls
    crawls = mongoengine.DictField()

    # public PGP key
    pgpKeys = mongoengine.ListField()

    # certificates
    certificates = mongoengine.ListField()

    # bitcoin Services
    bitcoinServices = mongoengine.DictField()

    # SSK keys
    sshKey = mongoengine.StringField()

    # SSH banner
    sshBanner = mongoengine.StringField()

    # FTP server fingerprint
    ftpFingerprint = mongoengine.StringField()

    # FTP banner
    ftpBanner = mongoengine.StringField()

    # SMTP server fingerprint
    smtpFingerprint = mongoengine.StringField()

    # SMTP banner
    smtpBanner = mongoengine.StringField()

    # last Action
    lastAction = mongoengine.StringField()

    # timedOut  
    timedOut = mongoengine.BooleanField()

    # error
    error = mongoengine.ListField()

    # identifier report
    identifierReport = mongoengine.DictField()

    # simple report
    simpleReport = mongoengine.DictField()
