#!venv/bin/python
from logging import debug, show
from Primaze import Protocol
from Primaze.ncbi import snp


def main(): 
    """Entry point of the sandbox"""
    __filename__ = __file__.split('/')[-1]
    show("Entry Point: {}\n".format(__filename__))

    # p = Protocol('data/procedure.yml')
    # p.compile()
    # p.execute()

    snp.main()
    
    show("End Point: {}\n".format(__filename__))