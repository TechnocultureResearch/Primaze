import sys
from yaml import load, dump
from pprint import pprint


file_data = load("""
name: Single Target PCR
specie: Homeo Sapiens
pipeline:
 - fetch_genome
 - gc_check_template
 - check_tm
""")


file_data1 = ("""
name: Single Target PCR
specie: Homeo Sapiens
pipeline:
 - fetch_genome
 - gc_check_template
 - check_tm
""")


def print_protocol(file_data):
    file_name = file_data['name']
    pretty_code = "\n{0}\n==={1}===\n{0}\n".format(
        '='*(len(file_name) + 6), file_name)
    pretty_code += dump(file_data, default_flow_style=False)
    print(pretty_code)
    return pretty_code


def fetch_genome():
    data = ['A', 'B']
    print(data)
    return data


def gc_check_template():
    return True


commands = {
    'fetch_genome': fetch_genome,
    'gc_check_template': gc_check_template
}


# pprint(file_data)
# print(file_data['name'])


def validate_protocol(protocol):
    valid = True
    try:
        for _ in protocol['pipeline']:
            if _ not in commands:
                raise SyntaxError("Command: {} is not recognized.".format(_))
    except SyntaxError as sErr:
        print(sErr, file=sys.stderr)
        exit(1)


def runner(protocol):
    return [commands[f]() for f in file_data['pipeline']]


print_protocol(file_data)
validate_protocol(file_data)
runner(file_data)
