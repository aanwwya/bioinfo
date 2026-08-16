dna = "ATGCGATCGATGCTAG"

complement = dna.translate(str.maketrans("ATGC", "TACG"))
reverse_complement = complement[::-1]

print("DNA:", dna)
print("Complement:", complement)
print("Reverse complement:", reverse_complement)

valid_bases = set("ATGC")
is_valid = all(base in valid_bases for base in dna)

print("Valid DNA:", is_valid)

print("Original length:", len(dna))
print("Reverse complement length:", len(reverse_complement))

double_reverse_complement = reverse_complement.translate(
    str.maketrans("ATGC", "TACG")
)[::-1]

print("Double reverse complement:", double_reverse_complement)
print("Matches original:", double_reverse_complement == dna)