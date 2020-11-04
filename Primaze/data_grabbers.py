""" data grabbers """
from logging import temp, debug
from Primaze import register


@register
def get_genome():
    temp("I got the genome")


@register
def validate_snp_region_on_target():
    temp("I did validate this snp region on the given target")


@register
def snp_id(*ids):
    temp("I did validate this snp region on the given target")


@register
def get_chromosome_location():
    temp("I did validate this snp region on the given target")


@register
def print_allele_frequency(*selectors):
    temp("I did validate this snp region on the given target")


@register
def select_target_region(width, symmetric=True):
    temp("I did validate this snp region on the given target")


@register
def generate_primer_pool(method="primer3"):
    temp("I did validate this snp region on the given target")


@register
def filter_primer_pool(GC, del_g, free_energy, thermo=False):
    temp("I did validate this snp region on the given target")
