#!venv/bin/python

""" main.py (Sandbox) : Entry Point of the project """
from Pricore import Core


def main():
    """ Entry point of the program """
    print(Core.version())
    print(Core.double(3.14))


if __name__ == '__main__':
    main()
