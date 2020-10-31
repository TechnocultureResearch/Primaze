#!venv/bin/python
from logging import info, debug, critical
from Sandbox import main
from Pricore import core

"""main.py : Entry Point of the project"""
core.init()

info('Entry point')
main()
info("Program Ends Without a Crash.")