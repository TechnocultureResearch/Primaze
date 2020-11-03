#!venv/bin/python
from logging import debug, show
from Primaze import Protocol
from Primaze.ncbi import get_snp_data, process_snp_data
from pprint import pprint


def main(): 
    """Entry point of the sandbox"""
    __filename__ = __file__.split('/')[-1]
    show("Entry Point: {}\n".format(__filename__))

    data = get_snp_data(3057)
    snp_info = process_snp_data(data)
    pprint(snp_info)

    p = Protocol('data/procedure.yml')
    # p.compile()
    # p.execute()

    # snp.main()
    
    show("End Point: {}\n".format(__filename__))