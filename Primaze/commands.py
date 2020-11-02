from logging import debug
from Primaze.core import available_commands, register


@register
def fetch_genome():
    data = ['A', 'B']
    debug(data)
    return data

@register
def gc_check_template():
    return True

@register
def check_length():
    return True

@register
def check_tm():
    pass