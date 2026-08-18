import time

from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord
from bioseq_engine.src.bioseq.dataset import find_motif


def create_dataset(record_count: int, sequence_length: int):
    records = []

    sequence = "ATGCGATCGATCGATCGATC" * (
        sequence_length // 20 + 1
    )
    sequence = sequence[:sequence_length]

    for i in range(record_count):
        records.append(
            FastaRecord(
                record_id=f"gene{i}",
                sequence=Sequence(sequence),
            )
        )

    return records


def benchmark():
    records = create_dataset(
        record_count=1000,
        sequence_length=1000,
    )

    start = time.perf_counter()

    for record in records:
        find_motif([record], "ATG")

    elapsed = time.perf_counter() - start

    print(f"records: {len(records)}")
    print(f"sequence length: {len(records[0].sequence)}")
    print(f"time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    benchmark()