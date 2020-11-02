#!venv/bin/python
from logging import debug, show
from Primaze import Protocol


def main(): 
    """Entry point of the sandbox"""
    
    show("Entry Point: {}\n".format(__file__))

    p = Protocol('data/procedure.yml')
    p.compile()
    p.execute()
    
    show("End Point: {}\n".format(__file__))