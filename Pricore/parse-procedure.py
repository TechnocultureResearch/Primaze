from yaml import load, dump
from pprint import pprint


file_data = load("""
name: Single Target PCR
specie: Homeo Sapiens
pipeline:
 - fetch_genome
 - gc_check_template
""")


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


pprint(file_data)
print(file_data['name'])
runner = lambda protocol: [commands[f]() for f in file_data['pipeline']]