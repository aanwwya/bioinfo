from src.bioseq.sequence import Sequence
from src.bioseq.validation import is_valid_dna
from src.bioseq.search import naive_search


dna = Sequence("ATGCGATC")

print(dna.sequence)
print(len(dna))

print(is_valid_dna("ATGCGATC"))
print(is_valid_dna("ATGCXYZ"))
print(is_valid_dna(""))
print(naive_search("ATGCGATCGATGCTAG", "ATG"))
print(naive_search("ATGCGATCGATGCTAG", "AAA"))
print(naive_search("ATG", "ATGCGATC"))