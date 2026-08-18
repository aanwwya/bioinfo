from bioseq_engine.src.bioseq.fasta_record import FastaRecord
from bioseq_engine.src.bioseq.trie import Trie


def naive_search(sequence, pattern):
    matches = []

    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i + len(pattern)] == pattern:
            matches.append(i)

    return matches


class MotifSearchEngine:
    VALID_BASES = frozenset("ACGT")

    def __init__(self, motifs: list[str]):
        if not motifs:
            raise ValueError("motifs cannot be empty")

        normalized_motifs = []

        for motif in motifs:
            motif = motif.upper()

            if not motif:
                raise ValueError("motif cannot be empty")

            invalid_bases = set(motif) - self.VALID_BASES

            if invalid_bases:
                raise ValueError(
                    f"invalid DNA bases in motif '{motif}': "
                    f"{sorted(invalid_bases)}"
                )

            normalized_motifs.append(motif)

        self.motifs = normalized_motifs
        self.trie = Trie()

        for motif in self.motifs:
            self.trie.insert(motif)

        self.trie.build_failure_links()

    def search_record(
        self,
        record: FastaRecord,
    ) -> dict[str, list[int]]:
        results = self.trie.search(
            record.sequence.sequence
        )

        matches = {
            motif: []
            for motif in self.motifs
        }

        for position, motif in results:
            matches[motif].append(position)

        return matches

    def search_dataset(
        self,
        records: list[FastaRecord],
    ) -> dict[str, dict[str, list[int]]]:
        results = {}

        for record in records:
            results[record.record_id] = self.search_record(
                record
            )

        return results