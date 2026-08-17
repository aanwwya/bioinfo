from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord


def _make_record(name, sequence_parts):
    if not name:
        raise ValueError("FASTA header cannot be empty")

    if not sequence_parts:
        raise ValueError(f"FASTA record '{name}' has no sequence")

    return FastaRecord(
        record_id=name,
        sequence=Sequence("".join(sequence_parts)),
    )


def parse_fasta(text: str) -> list[FastaRecord]:
    records = []
    name = None
    sequence_parts = []

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):
            if name is not None:
                records.append(
                    _make_record(name, sequence_parts)
                )

            name = line[1:].strip()
            sequence_parts = []

        else:
            if name is None:
                raise ValueError("FASTA sequence found before header")

            sequence_parts.append(line)

    if name is not None:
        records.append(
            _make_record(name, sequence_parts)
        )

    return records


def read_fasta(path: str):
    name = None
    sequence_parts = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if name is not None:
                    yield _make_record(name, sequence_parts)

                name = line[1:].strip()
                sequence_parts = []

            else:
                if name is None:
                    raise ValueError("FASTA sequence found before header")

                sequence_parts.append(line)

    if name is not None:
        yield _make_record(name, sequence_parts)