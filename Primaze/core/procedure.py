from logging import info, debug, fatal, error
from collections import deque
from termcolor import colored

from Primaze.core import available_commands


class Procedure:
    steps = deque()
    command_not_found = []
    _steps_data = []

    def __init__(self, _parsed_protocol):
        try:
            self._steps_data = _parsed_protocol['procedure'] # MAGIC STRING
        except KeyError as kErr:
            fatal(kErr)
            exit(1)
        debug(self)

    def compile(self):
        debug(available_commands)
        for _ in self._steps_data:
            if _ not in str(available_commands): 
                self.command_not_found.append(_)
            else:
                self.steps.append(_)
        err = len(self.command_not_found)
        if err:
            error("{} command{} from the procedure not found.".format(colored(err, 'red'), 's' if err > 1 else ''))
            error(self)
            exit(1)
        else:
            debug("Compilation Successfull.")

    __repr__ = lambda self: " -> ".join(
        [colored(_, 'red' if _ in self.command_not_found else 'green') for _ in self._steps_data])
    __len__ = lambda self: len(self._steps_data)
    run = lambda self: [debug(_) for _ in self.steps]