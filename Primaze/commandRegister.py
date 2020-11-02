from Primaze.Pricore.command import Command, CommandsDeque

from logging import debug, error
from collections import deque


# !
available_commands = CommandsDeque()


def register(f):
    debug("Command Registered: {} -> available_commands".format(f.__name__))
    available_commands.append(Command(f))
    return(f)