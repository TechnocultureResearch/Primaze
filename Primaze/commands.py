from logging import debug
from Primaze.commandRegister import available_commands
from Primaze.Pricore.command import Command

def fetch_genome():
    data = ['A', 'B']
    debug(data)
    return data


def gc_check_template():
    return True


available_commands.append(Command(fetch_genome))
available_commands.append(Command(gc_check_template))