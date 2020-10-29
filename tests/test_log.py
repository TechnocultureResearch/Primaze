import logging
from ProjectContext import log
from datetime import date, datetime, timedelta
import os


def test_init():
    assert os.path.exists("log/")
    try:
        log.init()
    except(FileNotFoundError):
        assert False
    assert os.path.exists("log/debug.log")
    

def test_delhi():
    assert (datetime.now() + timedelta(hours=5.5)).timetuple() == log.delhi(0, 0)
