from Primaze.core import Command, CommandsDeque
from collections import deque

# !
available_commands = CommandsDeque()

def register(f):
    available_commands.append(Command(f))
    return(f)
