class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence # storing dna sequence

    def __len__(self):
        return len(self.sequence) # return num of bases