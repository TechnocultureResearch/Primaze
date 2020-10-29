""" Core Functions """
from Pricore import log


def init():
    log.init()


def version():
    """ prints the version number formatted as a string """
    return "1.0.0"


def double(i):
    """ doubles a given value """
    return 2*i

