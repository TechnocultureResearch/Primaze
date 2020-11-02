from Primaze.Pricore.command import CommandsDeque
# from Primaze import commands

from logging import debug, error
from collections import deque


# !
available_commands = CommandsDeque()
# print(available_commands)

# def register(f):
#     debug("Command Registered: {} -> available_commands".format(f.__name__))
#     available_commands.append(Command(f))
#     return(f)


# for _ in commands:
#     print(_)