import logging

def initLogging():
    """ Logging configuration package """
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
                '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # set debugging to max level (DEBUG, CRITICAL, ERROR, WARNING or INFO )
    logger.setLevel(logging.DEBUG)
    return logger
