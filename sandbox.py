#!venv/bin/python

""" main.py (Sandbox) : Entry Point of the project """
from Pricore import Core
from Primaze import constraint


def main():
    """ Entry point of the program """
    print(Core.version())
    print(Core.double(3.14))
    constraint.constraint("4.5", 4.7)


if __name__ == '__main__':
    main()
