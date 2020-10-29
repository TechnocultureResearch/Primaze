""" Core Functions """
import logging


def init():
    logging.basicConfig(
        # filename='log.log', 
        format='(%(asctime)s) [%(levelname)s]: %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p',
        level=logging.INFO
    )
    logging.debug('Log initiated')


def version():
    """ prints the version number formatted as a string """
    logging.info('Logging info here')
    return "1.0.0"


def double(i):
    """ doubles a given value """
    return 2*i

