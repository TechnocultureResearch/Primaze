from logging import info, debug, fatal, error, temp
from collections import deque
from termcolor import colored

from Primaze.core import available_commands, Command, refresh_register


def has_a_list(_):
    return " - " in _


def has_params(_):
    return type(_) == type(dict())


def is_a_string(_):
    return type(_) == type('a')


def parse_list(_):
    return _.split(" - ")

def extract_dict_title(_):
    return list(_.keys())[0]


def get_step_title(_):
    if is_a_string(_):
        return parse_list(_)[0] if has_a_list(_) else _
    elif has_params(_):
        return extract_dict_title(_)
    else:
        error("Bad token type")
        exit(1)


def get_step_args(_):
    if is_a_string(_) and has_a_list(_):
        l = parse_list(_)
        del l[0]
        return l
    return list()


def get_step_kwargs(_):
    if has_params(_):
        return _[extract_dict_title(_)]
    return {}


class Procedure:
    steps = deque()
    commands_not_found = []
    _steps_data = []
    _steps_title = []
    _arg_fail = set()

    def __init__(self, _parsed_protocol):
        try:
            self._steps_data = _parsed_protocol['procedure'] # MAGIC STRING
        except KeyError as kErr:
            fatal(kErr)
            exit(1)

    def compile(self):
        refresh_register()
        debug("Available Commands: \n{}\n".format(available_commands))
        
        for _ in self._steps_data:
            # add to the steps title list
            fname = get_step_title(_) # debug(fname)
            self._steps_title.append(fname)

            if fname in available_commands: 
                command = available_commands.find(fname)

                args = get_step_args(_)
                kwargs = get_step_kwargs(_)

                # print(args)
                # print(kwargs)
                try:
                    command.validate(args, kwargs)
                except ValueError as vErr:
                    self._arg_fail.add(fname)
                    error("{}: {}".format(command, vErr))
                except TypeError as tErr:
                    self._arg_fail.add(fname)
                    error("{}: Attribute(s) Missing: {}".format(command, tErr))
                command.set_args(args, kwargs)

                self.steps.append(command)
                temp(repr(command))
            else:
                fatal(fname)
                self.commands_not_found.append(fname)
            
        err = len(self.commands_not_found)
        aerr = len(self._arg_fail)
        if err:
            error("{} command{} from the procedure not found.".format(colored(err, 'red'), 's' if err > 1 else ''))
        if aerr:
            error("{} command{} had an argument mismatch.".format(colored(aerr, 'yellow'), 's' if aerr > 1 else ''))
        if err + aerr:
            error(self)
            error(self._arg_fail)
            raise Exception("Compilation Failed Error")
            exit(1)
        
        debug(self)
        info("Compilation Successfull.\n")


    def __repr__(self):
        # print(self._arg_fail)
        return "Compiled Procedure: \n" + " -> ".join(
            [colored(_, 'red' if _ in self.commands_not_found else 'yellow' if _ in list(self._arg_fail) else 'green') 
            for _ in self._steps_title]) + "\n"

    __len__ = lambda self: len(self._steps_data)
    run = lambda self: [_() for _ in self.steps]