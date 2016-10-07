import logging

def initLogging():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
    #logger.debug('often makes a very good meal of %s', 'visiting tourists')