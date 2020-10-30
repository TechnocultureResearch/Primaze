#!venv/bin/python
from logging import info, debug, critical
from Sandbox import main
from Pricore import core


""" Entry point of the program """
core.init()

info('Entry point')
main()
info("Program Ends Without a Crash.")