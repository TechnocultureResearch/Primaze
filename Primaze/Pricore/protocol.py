import sys
from yaml import load, dump, FullLoader
from collections import namedtuple  
from .procedure import Procedure
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
        file_dump = dump(self.parsed_protocol, default_flow_style=False)
        bar = "{}".format('='*(len(self.name) + 8))
        title = "\n    {}    ".format(self.name)
        return "\n{0}{1}\n{0}\n{2}{0}".format(bar, title, file_dump)
    
    execute = lambda self: self.procedure.run()

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
