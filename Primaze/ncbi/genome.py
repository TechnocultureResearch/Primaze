#!./venv/bin/python
from typing import List, Set, Dict, Tuple, Optional, Callable
from decouple import config  # type: ignore
from os import listdir


def read_fasta(ch_num: int):  # Use context manager
    # TODO: unzip chromosome files
    pass


def fasta_value_at_loaction(ch_num: int, index: int) -> str:
    pass


def check_value_at_location(ch_num: int, index: int, value: str) -> bool:
    # fasta_value_at_loaction()
    # TODO: check snp location
    pass


def get_neighbors(ch_num: int, index: int, range: int) -> List[str]:
    # TODO: get neighbouring region
    pass
