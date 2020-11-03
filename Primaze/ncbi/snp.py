from logging import debug, show, temp
from Bio.Seq import Seq
from Bio import Align


# def main():
#     __filename__ = __file__.split('/')[-1]
#     show("Entry Point: {}".format(__filename__))

#     my_snp = 3057
#     record = SeqIO.read("NC_005816.gb", "genbank")
#     for feature in record.features:
#         if my_snp in feature:
#             temp("{} {}".format(feature.type, feature.qualifiers.get("db_xref")))

#     show("End of {}".format(__filename__))


def main():
    my_seq = Seq("ACTACTCATC")
    debug(my_seq)
    debug(my_seq.complement())
    debug(my_seq.reverse_complement())

    aligner = Align.PairwiseAligner(match_score=1.0)
    aligner.mode = 'local'
    debug(aligner.score(my_seq, my_seq.complement()))


    alignments = aligner.align(my_seq, my_seq.complement())
    for a in alignments:
        print(a)