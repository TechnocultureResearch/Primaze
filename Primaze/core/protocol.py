import sys
from logging import error, info, debug, fatal
from yaml import load, dump, FullLoader
from collections import namedtuple  

from Primaze.core import Procedure


class Protocol:
    file_name = ""
    parsed_protocol = []
    name = ""
    specie = ""
    procedure = None

    def __init__(self, file_name):
        self.file_name = file_name
        try:
            self.parsed_protocol = Protocol.parse_procedure_data(file_name)
            self.name = self.parsed_protocol['name']        # MAGIC STRING
            self.specie = self.parsed_protocol['specie']    # MAGIC STRING
        except (FileNotFoundError, KeyError) as err:
            fatal(err)
            exit(1)
        
        # debug(self)
        self.procedure = Procedure(self.parsed_protocol)

    def __repr__(self):
        file_dump = dump(self.parsed_protocol, default_flow_style=False)
        bar = "{}".format('='*(len(self.name) + 8))
        title = "\n    {}    ".format(self.name)
        return "\n{0}{1}\n{0}\n{2}{0}".format(bar, title, file_dump)
    
    __len__ = lambda self: len(self.procedure)
    execute = lambda self: self.procedure.run()
    def compile(self):
        try:
            self.procedure.compile()
        except Exception as e:
            error("Compilation Failed.")
            exit(1)

    @staticmethod
    def parse_procedure_data(file_name):
        try:
            return load(
                open(file_name),
                Loader=FullLoader
            )
        except FileNotFoundError as fErr:
            fatal(fErr)
            exit(1)
