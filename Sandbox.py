#!venv/bin/python
from logging import debug, show
from Primaze import Protocol
# from Primaze.ncbi import SNP
from pprint import pprint


def main(): 
    """Entry point of the sandbox"""
    __filename__ = __file__.split('/')[-1]
    show("Entry Point: {}\n".format(__filename__))


    # pitch_allele = SNP(3057)
    # composition_allele = SNP(3401)

    p = Protocol('data/procedure.yml')
    p.compile()
    p.execute()
    
    
    show("End Point: {}\n".format(__filename__))