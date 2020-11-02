from logging import debug
from Primaze import register


@register
def get_genome():
    debug("I got the genome")


@register
def validate_snp_region_on_target():
    debug("I did validate this snp region on the given target")


@register
def snp_id():
    debug("I did validate this snp region on the given target")


@register
def get_chromosome_location():
    debug("I did validate this snp region on the given target")


@register
def print_allele_frequency():
    debug("I did validate this snp region on the given target")


@register
def select_target_region():
    debug("I did validate this snp region on the given target")


@register
def generate_primer_pool():
    debug("I did validate this snp region on the given target")


@register
def filter_primer_pool():
    debug("I did validate this snp region on the given target")
