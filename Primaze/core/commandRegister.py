from Primaze.core.command import CommandsDeque, Command
from collections import deque

# !
available_commands = CommandsDeque()

def register(f):
    available_commands.append(Command(f))
    return(f)
