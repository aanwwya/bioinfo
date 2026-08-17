from dataclasses import dataclass

from bioseq_engine.src.bioseq.fasta_record import FastaRecord

from bioseq_engine.src.bioseq.kmp import kmp_search


@dataclass
class DatasetStats:
    record_count: int
    total_bases: int
    average_length: float
    shortest_length: int
    longest_length: int
    gc_content: float


def calculate_stats(records: list[FastaRecord]) -> DatasetStats:
    if not records:
        raise ValueError("records cannot be empty")

    lengths = [len(record.sequence) for record in records]
    total_bases = sum(lengths)

    gc_bases = sum(
        base in "GC"
        for record in records
        for base in record.sequence
    )

    return DatasetStats(
        record_count=len(records),
        total_bases=total_bases,
        average_length=total_bases / len(records),
        shortest_length=min(lengths),
        longest_length=max(lengths),
        gc_content=(gc_bases / total_bases) * 100,
    )
    
def longest_record(records: list[FastaRecord]) -> FastaRecord:
    if not records:
        raise ValueError("records cannot be empty")

    return max(records, key=lambda record: len(record.sequence))

def shortest_record(records: list[FastaRecord]) -> FastaRecord:
    if not records:
        raise ValueError("records cannot be empty")

    return min(records, key=lambda record: len(record.sequence))

def find_motif(
    records: list[FastaRecord],
    motif: str,
) -> dict[str, list[int]]:
    if not motif:
        raise ValueError("motif cannot be empty")

    results = {}

    for record in records:
        results[record.record_id] = kmp_search(
            record.sequence.sequence,
            motif.upper(),
        )

    return results