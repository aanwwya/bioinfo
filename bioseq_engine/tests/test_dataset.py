import pytest

from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.fasta_record import FastaRecord
from bioseq_engine.src.bioseq.dataset import calculate_stats


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