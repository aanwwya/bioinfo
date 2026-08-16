from collections import Counter

dna = "ATGCGATCGATGCTAG"

counts = Counter(dna)

print("DNA:", dna)
print("Length:", len(dna))
print("Counts:", counts)

gc_content = (counts["G"] + counts["C"]) / len(dna) * 100
print("GC content:", gc_content, "%")

valid_bases = set("ATGC")
is_valid = all(base in valid_bases for base in dna)

print("Valid DNA:", is_valid)

at_content = (counts["A"] + counts["T"]) / len(dna) * 100
print("AT content:", at_content, "%")


complement = dna.translate(str.maketrans("ATGC", "TACG"))
print("Complement:", complement)