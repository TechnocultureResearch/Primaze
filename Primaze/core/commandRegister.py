from Primaze.core import Command, CommandsDeque
from collections import deque

# !
available_commands = CommandsDeque()
to_register = []

def register(f):
    to_register.append(f)
    return(f)

def refresh_register():
    for func in to_register:
        available_commands.append(Command(func))