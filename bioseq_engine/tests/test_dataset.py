import pytest

from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord

from bioseq_engine.src.bioseq.dataset import (
    calculate_stats,
    longest_record,
    shortest_record,
    find_motif,
)


def test_calculate_stats():
    records = [
        FastaRecord("gene1", Sequence("ATGC")),
        FastaRecord("gene2", Sequence("GCGCTA")),
    ]

    stats = calculate_stats(records)

    assert stats.record_count == 2
    assert stats.total_bases == 10
    assert stats.average_length == 5.0
    assert stats.shortest_length == 4
    assert stats.longest_length == 6
    assert stats.gc_content == 60.0


def test_calculate_stats_empty():
    with pytest.raises(ValueError):
        calculate_stats([])


def test_longest_record():
    records = [
        FastaRecord("gene1", Sequence("ATGC")),
        FastaRecord("gene2", Sequence("ATGCGCTA")),
        FastaRecord("gene3", Sequence("ATGCGC")),
    ]

    result = longest_record(records)

    assert result.record_id == "gene2"
    assert result.sequence.sequence == "ATGCGCTA"


def test_longest_record_empty():
    with pytest.raises(ValueError):
        longest_record([])


def test_shortest_record():
    records = [
        FastaRecord("gene1", Sequence("ATGC")),
        FastaRecord("gene2", Sequence("ATGCGCTA")),
        FastaRecord("gene3", Sequence("ATG")),
    ]

    result = shortest_record(records)

    assert result.record_id == "gene3"
    assert result.sequence.sequence == "ATG"


def test_shortest_record_empty():
    with pytest.raises(ValueError):
        shortest_record([])


def test_find_motif():
    records = [
        FastaRecord(
            record_id="gene1",
            sequence=Sequence("ATGCGATG"),
        ),
        FastaRecord(
            record_id="gene2",
            sequence=Sequence("TTAA"),
        ),
    ]

    results = find_motif(records, "ATG")

    assert results == {
        "gene1": [0, 5],
        "gene2": [],
    }