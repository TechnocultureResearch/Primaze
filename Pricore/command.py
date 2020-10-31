available_commands = list()
def register(f):
    available_commands.append()
    return(f)

def fetch_genome():
    data = ['A', 'B']
    print(data)
    return data


def gc_check_template():
    return True


# Command = namedtuple('Command', [name, func])
# c = Command('fetch_genome', fetch_genome)