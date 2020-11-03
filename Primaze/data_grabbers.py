""" data grabbers """
from logging import show
from Primaze import register


@register
def get_genome():
    show("I got the genome")


@register
def validate_snp_region_on_target():
    show("I did validate this snp region on the given target")


@register
def snp_id():
    show("I did validate this snp region on the given target")


@register
def get_chromosome_location():
    show("I did validate this snp region on the given target")


@register
def print_allele_frequency():
    show("I did validate this snp region on the given target")


@register
def select_target_region():
    show("I did validate this snp region on the given target")


@register
def generate_primer_pool():
    show("I did validate this snp region on the given target")


@register
def filter_primer_pool():
    show("I did validate this snp region on the given target")
