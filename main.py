#!venv/bin/python
from logging import debug
from Sandbox import main
from Primaze.core import core

"""main.py : Entry Point of the project"""
core.init()

debug('Entry point')
main()
debug("Program Ends Without a Crash.")