from .Pricore.command import register, available_commands


@register
def fetch_genome():
    data = ['A', 'B']
    print(data)
    return data


@register
def gc_check_template():
    return True


if __name__=='__main__':
    print(available_commands)