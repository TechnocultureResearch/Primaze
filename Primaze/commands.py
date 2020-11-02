from Primaze.commandRegister import register

from logging import debug


@register
def fetch_genome():
    data = ['A', 'B']
    debug(data)
    return data


@register
def gc_check_template():
    return True