import time

from bioseq_engine.src.bioseq.kmp import kmp_search
from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord
from bioseq_engine.src.bioseq.trie import Trie

from bioseq_engine.benchmarks.comparison import (
    BenchmarkResult,
    print_comparison,
)


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


def benchmark_kmp(records, motifs):
    start = time.perf_counter()

    for record in records:
        sequence = record.sequence.sequence

        for motif in motifs:
            kmp_search(sequence, motif)

    return time.perf_counter() - start


def benchmark_aho_corasick(records, motifs):
    trie = Trie()

    for motif in motifs:
        trie.insert(motif)

    trie.build_failure_links()

    start = time.perf_counter()

    for record in records:
        trie.search(record.sequence.sequence)

    return time.perf_counter() - start


def main():
    records = create_dataset()

    results = []

    for motif_count in [8, 16, 32, 64, 128]:
        motifs = generate_motifs(motif_count)

        kmp_time = benchmark_kmp(records, motifs)

        aho_time = benchmark_aho_corasick(
            records,
            motifs,
        )

        results.append(
            BenchmarkResult(
                motif_count=motif_count,
                kmp_time=kmp_time,
                aho_corasick_time=aho_time,
            )
        )

    print_comparison(results)


if __name__ == "__main__":
    main()