#!venv/bin/python

# Sequence of imports matter
from Primaze.core import core
from logging import show
from Sandbox import main

"""main.py : Entry Point of the project"""
core.init()


show("Entry point: main.py")
main()
show("End of main.py")
