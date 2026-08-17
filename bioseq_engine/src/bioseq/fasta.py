from bioseq_engine.src.bioseq.sequence import Sequence


def parse_fasta(text: str) -> list[tuple[str, Sequence]]:
    records = []
    name = None
    sequence_parts = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            if name is not None:
                sequence = "".join(sequence_parts)
                records.append((name, Sequence(sequence)))

            name = line[1:].strip()
            sequence_parts = []

        else:
            if name is None:
                raise ValueError("FASTA sequence found before header")

            sequence_parts.append(line)

    if name is not None:
        sequence = "".join(sequence_parts)
        records.append((name, Sequence(sequence)))

    return records