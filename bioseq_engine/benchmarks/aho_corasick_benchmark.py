import time

from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord
from bioseq_engine.src.bioseq.trie import Trie


def create_dataset(record_count=1000, sequence_length=1000):
    records = []

    sequence = "ATGCGATCGATCGATCGATC" * (
        sequence_length // 20
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


def generate_motifs(count):
    bases = ["A", "T", "G", "C"]

    motifs = []

    for i in range(count):
        motif = ""

        value = i

        for _ in range(4):
            motif += bases[value % 4]
            value //= 4

        motifs.append(motif)

    return motifs


def benchmark():
    records = create_dataset()

    motif_counts = [8, 16, 32, 64, 128]

    for count in motif_counts:
        motifs = generate_motifs(count)

        trie = Trie()

        for motif in motifs:
            trie.insert(motif)

        start = time.perf_counter()

        total_matches = 0

        for record in records:
            matches = trie.search(record.sequence.sequence)
            total_matches += len(matches)

        elapsed = time.perf_counter() - start

        print(
            f"motifs: {count:3d} | "
            f"matches: {total_matches:8d} | "
            f"time: {elapsed:.6f} seconds"
        )


if __name__ == "__main__":
    benchmark()