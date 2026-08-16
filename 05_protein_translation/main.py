dna = "ATGCGATCGATGCTAG"

codon_table = {
    "ATG": "Methionine (M)",
    "CGA": "Arginine (R)",
    "TCG": "Serine (S)",
    "CTA": "Leucine (L)"
}
codons = [dna[i:i+3] for i in range(0, len(dna) - 2, 3)]

protein = [codon_table[codon] for codon in codons]

print("DNA:", dna)
print("Codons:", codons)
print("Protein:", protein)


for codon, amino_acid in zip(codons, protein):
    print(codon, "->", amino_acid)