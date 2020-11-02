#!venv/bin/python
from logging import info, debug, critical, error
from Primaze import Protocol


def main(): 
    """Entry point of the program"""
    try:
        p = Protocol('data/procedure.pz')
    except FileNotFoundError as fErr:
        error(fErr)
        exit(1)
    p.compile()
    
    debug("End of Main.")