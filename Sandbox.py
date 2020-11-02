#!venv/bin/python
from logging import info, debug, critical, error
from Primaze import Protocol


def main(): 
    """Entry point of the sandbox"""
    debug("Entry Point: {}\n".format(__file__))

    p = Protocol('data/procedure.yml')
    p.compile()
    p.execute()
    
    debug("End Point: {}\n".format(__file__))