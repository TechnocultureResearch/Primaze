""" Core Functions """
import logging
from sys import stdout
import datetime


def delhi(sec, what):
    '''sec and what is unused.'''
    delhi_time = datetime.datetime.now() + datetime.timedelta(hours=5.5)
    return delhi_time.timetuple()


def init():
    logging.basicConfig(
        level=logging.DEBUG, # DEBUG < INFO < WARNING < ERROR < CRITICAL
        format='%(asctime)s [%(levelname)s]: %(filename)s:%(funcName)s() - %(message)s',
        datefmt='%I:%M%p', # %d/%m/%Y 
        handlers=[
            logging.FileHandler("log/debug.log"),
            logging.StreamHandler(stdout)
        ]
    )
    logging.Formatter.converter = delhi

    logging.info('{}'.format('='*50))
    logging.info('Log initiated: {}'.format(datetime.date.today()))
