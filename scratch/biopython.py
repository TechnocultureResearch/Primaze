from Bio.Seq import Seq
from Bio import Align

my_seq = Seq("ACTACTCATC")
print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())

aligner = Align.PairwiseAligner(match_score=1.0)
aligner.mode = "local"
print(aligner.score(my_seq, my_seq.complement()))


alignments = aligner.align(my_seq, my_seq.complement())
for a in alignments:
    print(a)

# ===
