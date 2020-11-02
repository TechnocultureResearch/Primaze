from ProjectContext import procedure
from yaml import load, dump, FullLoader
from termcolor import colored


def get_data():
    return load("""
            name: NAME
            specie: SPECIE
            procedure:
                - STEP1
                - STEP2
        """, 
        Loader=FullLoader)


def test_init():
    data = get_data()
    
    assert data['name'] == 'NAME'
    assert data['specie'] == 'SPECIE'
    assert data['procedure'] == ['STEP1', 'STEP2']
    assert len(data['procedure']) == 2

    p = procedure.Procedure(data)
    assert p._steps_data == ['STEP1', 'STEP2']


def test_compile():
    data = get_data()
    p = procedure.Procedure(data)
    # p.compile()
    print(len(p.command_not_found))


def test_repr():
    data = get_data()

    p = procedure.Procedure(data)
    assert repr(p) == "{} -> {}".format(colored('STEP1', 'green'), colored('STEP2', 'green'))
    # print("{} -> {}".format(colored('STEP1', 'green'), colored('STEP2', 'green')))
    # print(repr(p))


def test_len():
    data = get_data()
    p = procedure.Procedure(data)
    assert len(p) == 2


def test_run():
    pass
    # raise NotImplementedError


if __name__ == "__main__":
    print("{} : {}".format(__file__, __name__))
    test_init()
    test_repr()
    test_len()
    test_compile()
    test_run()