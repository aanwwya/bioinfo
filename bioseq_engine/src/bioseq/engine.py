from bioseq_engine.src.bioseq.fasta import read_fasta
from bioseq_engine.src.bioseq.search import MotifSearchEngine


class BioSequenceEngine:
    def __init__(self, motifs: list[str]):
        self.search_engine = MotifSearchEngine(motifs)

    def search_file(self, path: str):
        records = read_fasta(path)

        results = {}

        for record in records:
            results[record.record_id] = (
                self.search_engine.search_record(record)
            )

        return results