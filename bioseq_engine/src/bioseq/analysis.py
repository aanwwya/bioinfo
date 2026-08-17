from bioseq_engine.src.bioseq.sequence import Sequence


def nucleotide_composition(sequence: Sequence) -> dict[str, int]:
    counts = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }

    for base in sequence:
        counts[base] += 1

    return counts


def gc_content(sequence: Sequence) -> float:
    composition = nucleotide_composition(sequence)

    gc_count = composition["G"] + composition["C"]

    return (gc_count / len(sequence)) * 100