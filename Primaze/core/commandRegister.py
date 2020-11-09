from Primaze.core import Command, CommandsDeque
from collections import deque
from inspect import signature

# !
available_commands = CommandsDeque()
to_register = []


def register(f):
    to_register.append(f)
    return f


get_args_spec = lambda f: str(signature(f)).replace(" ", "").strip("()").split(",")


def refresh_register():
    for func in to_register:
        available_commands.append(Command(func, get_args_spec(func)))
