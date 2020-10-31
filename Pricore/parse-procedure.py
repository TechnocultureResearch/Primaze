import sys
from yaml import load, dump, FullLoader
# from collections import namedtuple  
from logging import info, fatal


class Protocol:
    file_name = ""
    parsed_protocol = []
    name = ""
    specie = ""
    procedure = None

    def __init__(self, file_name):
        self.file_name = file_name
        self.parsed_protocol = Protocol.get_procedure_data(file_name)
        self.procedure = Procedure(self.parsed_protocol)
        
        try:
            self.name = self.parsed_protocol['name']        # MAGIC STRING
            self.specie = self.parsed_protocol['specie']    # MAGIC STRING
        except KeyError as kErr:
            fatal(kErr)
            exit(1)

    def __repr__(self):
        pretty_code = "\n{0}\n=== {1} ===\n{0}\n".format(
            '='*(len(self.name) + 8), self.name)
        pretty_code += dump(self.parsed_protocol, default_flow_style=False)
        return pretty_code

    @staticmethod
    def get_procedure_data(file_name):
        try:
            return load(
                open(file_name),
                Loader=FullLoader
            )
        except FileNotFoundError as fErr:
            fatal(fErr)
            exit(1)


# Command = namedtuple('Command', [name, func])
# c = Command('fetch_genome', fetch_genome)

class Command(namedtuple):
    def __init__(self, members): super().__init__(members)

    def __repr__(self):
        return self.name

available_commands = list()
def register(f):
    available_commands.append()
    return(f)

def fetch_genome():
    data = ['A', 'B']
    print(data)
    return data


def gc_check_template():
    return True


class Procedure:
    command_names = list()
    commands = list()

    def __init__(self, parsed_protocol):
        try:
            self.command_names = parsed_protocol['procedure'] # MAGIC STRING
        except KeyError as kErr:
            print("FATAL: {}".format(kErr))
            exit(1)

        self.validate_procedure()

    def validate_procedure(self):
        try:
            for _ in self.command_names:
                if _ not in self.commands:
                    raise SyntaxError(
                        "Command: {} is not recognized.".format(_))
        except SyntaxError as sErr:
            print(sErr)
            exit(1)
    
    def run(self):
        try:
            return [commands[f]() for f in procedure_data['pipeline']]
        except KeyError as kErr:
            print("FATAL: {}".format(kErr))
            exit(1)


p = Protocol("data/procedure.yml")
print(p)
p.run()
