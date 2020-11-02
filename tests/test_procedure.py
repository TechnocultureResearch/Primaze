from ProjectContext import procedure
from yaml import load, dump, FullLoader


def test_procedure_init():
    data = load("""
            name: NAME
            specie: SPECIE
            procedure:
                - STEP1
                - STEP2
        """, 
        Loader=FullLoader)
    
    assert data['name'] == 'NAME'
    assert data['specie'] == 'SPECIE'
    assert data['procedure'] == ['STEP1', 'STEP2']
    assert len(data['procedure']) == 2

    p = procedure.Procedure(data)
    assert p._steps_data == ['STEP1', 'STEP2']


if __name__ == "__main__":
    test_procedure_init()