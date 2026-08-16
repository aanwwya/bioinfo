dna = "ATGCGATCGATGCTAG"

rna = dna.replace("T", "U")

print("DNA:", dna)
print("RNA:", rna)

valid_bases = set("ATGC")
is_valid = all(base in valid_bases for base in dna)

print("Valid DNA:", is_valid)
print("RNA length:", len(rna))

valid_rna_bases = set("AUGC")
is_valid_rna = all(base in valid_rna_bases for base in rna)

print("Valid RNA:", is_valid_rna)
print("T in DNA:", dna.count("T"))
print("U in RNA:", rna.count("U"))