def is_valid_dna(sequence):
    valid_bases = set("ATGC") # valid dna bases
    return bool(sequence) and all(base.upper() in valid_bases for base in sequence)
# reject invalid or empty seq