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

    # WEB service detected
    webDetected = mongoengine.BooleanField()

    # TLS ciphering detected
    tlsDetected = mongoengine.BooleanField()

    # pprivate key
    privateKeyDetected = mongoengine.BooleanField()

    # Skynet detected
    skynetDetected = mongoengine.BooleanField()

    # certificate
    certificates = mongoengine.ListField()

    # Time out
    TimedOut = mongoengine.BooleanField()

    # last Action
    lastAction = mongoengine.StringField()

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


    serverPoweredBy = mongoengine.StringField()

    # WEB server version
    serverVersion = mongoengine.StringField()
    foundApacheModStatus = mongoengine.BooleanField()
    relatedOnionServices = mongoengine.ListField()
    relatedOnionDomains = mongoengine.ListField()
    linkedSites = mongoengine.ListField()
    internalPages = mongoengine.ListField()

    # IP address
    ipAddresses = mongoengine.ListField()
    openDirectories = mongoengine.ListField()

    # exif metadata
    exifImages = mongoengine.ListField()

    # interesting files
    interestingFiles = mongoengine.ListField()
    pageReferencedDirectories = mongoengine.ListField()

    # public PGP key
    pgpKeys = mongoengine.ListField()

    # hashes detected
    hashes = mongoengine.ListField()

    # content of WEB page
    snapshot = mongoengine.StringField()

    # title of WEB page
    pageTitle = mongoengine.StringField()

    responseHeaders = mongoengine.DictField()

    # public Bitcoin address
    bitcoinAddresses = mongoengine.ListField()

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
