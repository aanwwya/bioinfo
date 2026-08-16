dna = "ATGCGATCGATGCTAG"

codons = [dna[i:i+3] for i in range(0, len(dna) - 2, 3)]

print("DNA:", dna)
print("Codons:", codons)

remainder = len(dna) % 3

print("Incomplete bases:", remainder)
print("Number of complete codons:", len(codons))

for i, codon in enumerate(codons, start=1):
    print(f"Codon {i}: {codon}")