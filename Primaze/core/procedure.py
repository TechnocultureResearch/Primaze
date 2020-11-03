from logging import info, debug, fatal, error, warn
from collections import deque
from termcolor import colored

from Primaze.core import available_commands, Command, refresh_register


class Procedure:
    steps = deque()
    commands_not_found = []
    _steps_data = []
    _steps_title = []

    def __init__(self, _parsed_protocol):
        try:
            self._steps_data = _parsed_protocol['procedure'] # MAGIC STRING
        except KeyError as kErr:
            fatal(kErr)
            exit(1)
    

    @staticmethod
    def get_step_name(_): # debug(_)
        if type(_) == type('a'):
            return _
        elif type(_) == type(dict()): # debug(type(_))
            title = list(_.keys())[0]
            return title
        else:
            error("Bad token type")
            exit(1)


    def compile(self):
        refresh_register()
        debug("Available Commands: \n{}\n".format(available_commands))
        for _ in self._steps_data:
            # add to the steps title list
            fname = Procedure.get_step_name(_) # debug(fname)
            self._steps_title.append(fname)

            if fname in available_commands: 
                index = available_commands.find(fname)
                self.steps.append(index)
            else:
                fatal(fname)
                self.commands_not_found.append(fname)
            
        err = len(self.commands_not_found)
        if err:
            error("{} command{} from the procedure not found.".format(colored(err, 'red'), 's' if err > 1 else ''))
            error(self)
            exit(1)
        else:
            debug(self)
            info("Compilation Successfull.\n")


    def __repr__(self):
        return "Compiled Procedure: \n" + " -> ".join([colored(_, 'red' if _ in self.commands_not_found else 'green') for _ in self._steps_title]) + "\n"
    __len__ = lambda self: len(self._steps_data)
    run = lambda self: [_() for _ in self.steps]