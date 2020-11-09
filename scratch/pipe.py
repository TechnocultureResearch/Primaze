class Primer:
    seq = ""
    len = 0

    def __init__(self, seq):
        self.seq = seq
        self.len = len(seq)
        print(self)

    def __len__(self):
        return self.len

    def __repr__(self):
        return "[Sequence: {}; len: {}]".format(self.seq, self.len)

    def __getitem__(self, item):
        return self.seq[item]


primers = list()
primers.append(Primer("HAGFSH"))
primers.append(Primer("JJAGHSJGHSA"))


# def procedure(f):
#     return lambda f: print(f(_))

# @procedure
# def filter(_):
#     return _[0]

# @procedure
# def visualize(_):
#     return "{}\n{}\n{}".format(_, '|'*len(_), _)

# procedure = [filter, visualize]
# [f(primers) for f in procedure]
