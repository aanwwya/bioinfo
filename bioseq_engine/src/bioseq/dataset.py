from dataclasses import dataclass

from bioseq_engine.src.bioseq.fasta_record import FastaRecord


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