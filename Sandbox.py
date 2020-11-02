#!venv/bin/python
from logging import info, debug, critical, error
from Primaze.Pricore.protocol import Protocol
# from Primaze.Pricore.command import Command
# from Primaze.commands import fetch_genome, gc_check_template


def main(): 
    """Entry point of the program"""
    try:
        p = Protocol('data/procedure.pz')
    except FileNotFoundError as fErr:
        error(fErr)
        exit(1)
    except BaseException as Err:
        error(Err)
        exit(1)
    
    # ...
