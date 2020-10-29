#!venv/bin/python
from logging import info, debug, critical


""" main.py (Sandbox) : Entry Point of the project """
from Pricore import core
from Primaze.constraint import constraint


def main():
    """ Entry point of the program """
    info('Entry point')

    c1 = constraint("4.5", 4.7)
    debug(c1)



if __name__ == '__main__':
    core.init()

    try:
        main()
    except:
        # Top level Exception
        critical('main program crashed')
        exit(1)
