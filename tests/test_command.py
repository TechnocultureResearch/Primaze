import logging
from ProjectContext import log

from ProjectContext import CommandDeque, Command


def test_Command():
    func = lambda a: True
    c = Command(func)
    assert c.name == 'a'
