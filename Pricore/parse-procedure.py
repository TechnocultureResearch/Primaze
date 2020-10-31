import sys
from yaml import load, dump, FullLoader
from pprint import pprint


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
        
    
    def __repr__(self):
        pretty_code = "\n{0}\n=== {1} ===\n{0}\n".format('='*(len(self.name) + 8), self.name)
        pretty_code += dump(self.name, default_flow_style=False)
        return pretty_code


    @staticmethod
    def get_procedure_data(file_name):
        return load(
            open(file_name),
            Loader = FullLoader
        )


class Command:
    name = ""
    function = None

    def __init__(self, name, f):
        self.name = name
        self.function = f
    
    def __repr__(self):
        return self.name


class Procedure:
    raw_procedure = []
    commands = {
        Command('fetch_genome', fetch_genome),
        Command('gc_check_template', gc_check_template)
    }


    def __init__(self, parsed_protocol):
        try:
            self.raw_procedure = parsed_protocol['procedure']
        except KeyError as kErr:
            print("FATAL: {}".format(kErr))
            exit(1)
        
        self.validate_procedure()
    

    def validate_procedure(self):
        try:
            for _ in self.raw_procedure:
                if _ not in self.commands: raise SyntaxError("Command: {} is not recognized.".format(_))
        except SyntaxError as sErr:
            print(sErr)
            exit(1)




def fetch_genome():
    data = ['A', 'B']
    print(data)
    return data
    

def gc_check_template(cls):
    return True


# def validate_protocol(protocol):
#     try:
#         for _ in protocol:
#             if _ not in commands: raise SyntaxError("Command: {} is not recognized.".format(_))
#     except SyntaxError as sErr:
#         print(sErr)
#         exit(1)


def runner(procedure_data):
    try:
        return [commands[f]() for f in procedure_data['pipeline']]
    except KeyError as kErr:
        print("FATAL: {}".format(kErr))
        exit(1)



# commands = 

# print_protocol(file_data)
# validate_protocol(file_data)
# runner(file_data)


# procedure = get_procedure_data("data/procedure.yml")
p = Protocol("data/procedure.yml")
# print_protocol(procedure)
