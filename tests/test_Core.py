""" Test Cases for Core.Core functions """
from ProjectContext import core


def test_double():
    """ Tests Core.double function """
    assert core.double(2) == 4


def test_double_again():
    assert core.double(2.21111) == 4.42222


def test_version():
    assert core.version() == "1.0.0"
