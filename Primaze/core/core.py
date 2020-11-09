"""Core Functions"""
import sys
from Primaze.core import log


def init():
    print("System Version: {}".format(sys.version))
    assert sys.version_info.major == 3, "This tool supports python3 only."
    assert sys.version_info.minor >= 5, "This tool supports python3.5 or above."

    log.init()
