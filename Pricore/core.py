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
        format='(%(asctime)s) [%(levelname)s]: %(message)s    <===[%(filename)s(%(lineno)i)::%(funcName)s()]',
        datefmt='%I:%M:%S %p', # %d/%m/%Y 
        handlers=[
            logging.FileHandler("log/debug.log"),
            logging.StreamHandler(stdout)
        ]
    )
    logging.Formatter.converter = delhi

    logging.info('{}'.format('='*50))
    logging.info('Log initiated: {}'.format(datetime.date.today()))


def version():
    """ prints the version number formatted as a string """
    return "1.0.0"


def double(i):
    """ doubles a given value """
    return 2*i

