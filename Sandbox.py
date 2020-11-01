#!venv/bin/python
from logging import info, debug, critical
from Primaze.Pricore.protocol import Protocol
# from Primaze.Pricore.command import Command
# from Primaze.commands import fetch_genome, gc_check_template


def main(): 
    """Entry point of the program"""
    p = Protocol('data/procedure.pz')
    p.execute()