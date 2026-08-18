from bioseq_engine.src.bioseq.search import MotifSearchEngine
from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord


def test_search_record():
    engine = MotifSearchEngine(
        ["ATG", "GCG"]
    )

    record = FastaRecord(
        "gene1",
        Sequence("ATGCGATG"),
    )

    results = engine.search_record(record)

    assert results == {
        "ATG": [0, 5],
        "GCG": [2],
    }


def test_search_dataset():
    engine = MotifSearchEngine(
        ["ATG", "GCG"]
    )

    records = [
        FastaRecord(
            "gene1",
            Sequence("ATGCGATG"),
        ),
        FastaRecord(
            "gene2",
            Sequence("GCGAAA"),
        ),
    ]

    results = engine.search_dataset(records)

    assert results == {
        "gene1": {
            "ATG": [0, 5],
            "GCG": [2],
        },
        "gene2": {
            "ATG": [],
            "GCG": [0],
        },
    }


def test_search_record_with_no_matches():
    engine = MotifSearchEngine(
        ["ATG", "GCG"]
    )

    record = FastaRecord(
        "gene1",
        Sequence("TTTTTT"),
    )

    results = engine.search_record(record)

    assert results == {
        "ATG": [],
        "GCG": [],
    }


def test_empty_motifs():
    try:
        MotifSearchEngine([])
        assert False
    except ValueError:
        assert True