"""Log Functions"""
import logging
from functools import partial, partialmethod
from sys import stdout
from decouple import config
from datetime import date, datetime, timedelta


def addLogger(name, level):
    exec("logging.{0} = {1}".format( name.upper(), level ))
    eval("logging.addLevelName(logging.{0}, '{0}')".format( name.upper() ))
    exec("logging.Logger.{0} = partialmethod(logging.Logger.log, logging.{1})".format( name.lower(), name.upper() ))
    exec("logging.{0} = partial(logging.log, logging.{1})".format( name.lower(), name.upper() ))

addLogger('show', 5)
addLogger('temp', 2)


def init():
    level = config('LOGLEVEL') if config('LOGLEVEL') is not None else logging.DEBUG
    logging.basicConfig(
        level=level, # DEBUG < INFO < WARNING < ERROR < CRITICAL
        format='%(asctime)s [%(levelname)s]: %(filename)s(%(lineno)s):%(funcName)s() - %(message)s',
        datefmt='%I:%M%p',  # %d/%m/%Y
        handlers=[
            logging.FileHandler("log/debug.log"),
            logging.StreamHandler(stdout)
        ]
    )
    logging.Formatter.converter = delhi

    logging.info('{}'.format('='*50))
    logging.critical('Log initiated: {}'.format(date.today()))


# Helpers
def delhi(sec, what):
    """sec and what is unused."""
    delhi_time = datetime.now() + timedelta(hours=5.5)
    return delhi_time.timetuple()
