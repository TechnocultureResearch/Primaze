#!venv/bin/python
from logging import info, debug, critical
from Primaze.Pricore.protocol import Protocol


def main(): 
    """Entry point of the program"""
    p = Protocol('data/procedure.pz')
    debug(p.procedure)
    debug(p)
    p.execute()