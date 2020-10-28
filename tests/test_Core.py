""" Test Cases for Core.Core functions """
from ProjectContext import Core


def test_double():
    """ Tests Core.double function """
    assert Core.double(2) == 4

def test_double_again():
    assert Core.double(2.21111) == 4.42222

