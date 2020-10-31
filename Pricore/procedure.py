from logging import info, debug, fatal, error
from collections import deque
# from Pricore.command import Command
from termcolor import colored


commands = ['fetch_genome', 'gc_check_template', 'check_tm']

class Procedure:
    command_names = list()
    # command_queue = deque()

    def __init__(self, _parsed_protocol):
        try:
            self.command_names = _parsed_protocol['procedure'] # MAGIC STRING
        except KeyError as kErr:
            fatal(kErr)
            exit(1)

        self.validate_procedure()


    def validate_procedure(self):
        command_not_found = []
        for _ in self.command_names:
            if _ not in commands: 
                command_not_found.append(_)
        err = len(command_not_found)
        if err:
            error("{} command{} from the procedure not found.".format(colored(err, 'red'), 's' if err > 1 else ''))
            error(" -> ".join([colored(_, 'red' if _ in command_not_found else 'green') for _ in self.command_names]))
            exit(1)

    def __repr__(self):
        return " -> ".join(self.command_names)

    def run(self):
        try:
            info('Executing produce: ')
            # return [commands[f]() for f in procedure_data['pipeline']]
        except KeyError as kErr:
            fatal(kErr)
            exit(1)