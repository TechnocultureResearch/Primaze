from logging import debug, error
from collections import deque


class CommandsDeque(deque):
    __init__ = lambda self, iterable=[]: deque.__init__(self, iterable) # , maxlen=100)
    __contains__ = lambda self, name: any([name is str(c) for c in self])


# !
available_commands = CommandsDeque()


def register(f):
    debug("Command Registered: {} -> available_commands".format(f.__name__))
    available_commands.append(Command(f))
    return(f)


class Command():
    def __init__(self, func):
        self.func = func
    __repr__ = lambda self: "Command<{}>".format(str(self))
    __str__ = lambda self: self.func.__name__
    __call__ = lambda self: self.func()
    # is_available = lambda self: self.name in available_commands