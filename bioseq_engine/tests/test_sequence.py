import pytest

from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.validation import is_valid_dna
from bioseq_engine.src.bioseq.search import naive_search
from bioseq_engine.src.bioseq.kmp import build_lps, kmp_search
from bioseq_engine.src.bioseq.analysis import (
    nucleotide_composition,
    gc_content,
)
from bioseq_engine.src.bioseq.fasta import parse_fasta, read_fasta
from bioseq_engine.src.bioseq.fasta_record import FastaRecord


def test_sequence():
    dna = Sequence("ATGCGATC")

    assert dna.sequence == "ATGCGATC"
    assert len(dna) == 8


def test_sequence_invalid():
    with pytest.raises(ValueError):
        Sequence("")


def test_sequence_invalid_bases():
    with pytest.raises(ValueError):
        Sequence("ATGCXYZ")


def test_sequence_wrong_type():
    with pytest.raises(TypeError):
        Sequence(123)


def test_dna_validation():
    assert is_valid_dna("ATGCGATC") is True
    assert is_valid_dna("ATGCXYZ") is False
    assert is_valid_dna("") is False


def test_naive_search():
    assert naive_search("ATGCGATCGATGCTAG", "ATG") == [0, 9]
    assert naive_search("ATGCGATCGATGCTAG", "AAA") == []
    assert naive_search("ATG", "ATGCGATC") == []


def test_build_lps():
    assert build_lps("ATAT") == [0, 0, 1, 2]


def test_kmp_search():
    assert kmp_search("ATGCGATCGATGCTAG", "ATG") == [0, 9]


def test_searches_match():
    sequence = "ATGCGATCGATGCTAG"
    patterns = ["ATG", "GAT", "TAG", "AAA"]

    for pattern in patterns:
        assert naive_search(sequence, pattern) == kmp_search(
            sequence, pattern
        )


def test_sequence_indexing():
    dna = Sequence("ATGCGATC")

    assert dna[0] == "A"
    assert dna[3] == "C"


def test_sequence_slicing():
    dna = Sequence("ATGCGATC")
    result = dna[2:6]

    assert isinstance(result, Sequence)
    assert result.sequence == "GCGA"


def test_sequence_iteration():
    dna = Sequence("ATGC")

    assert list(dna) == ["A", "T", "G", "C"]


def test_gc_content():
    dna = Sequence("ATGCGATC")

    assert gc_content(dna) == 50.0


def test_nucleotide_composition():
    dna = Sequence("ATGCGATC")

    assert nucleotide_composition(dna) == {
        "A": 2,
        "C": 2,
        "G": 2,
        "T": 2,
    }


def test_analysis_gc_content():
    dna = Sequence("ATGCGATC")

    assert gc_content(dna) == 50.0


def test_parse_fasta():
    text = """>gene1
ATGC
>gene2
TTAA
"""

    records = parse_fasta(text)

    assert len(records) == 2
    assert records[0].record_id == "gene1"
    assert records[0].sequence.sequence == "ATGC"
    assert records[1].record_id == "gene2"
    assert records[1].sequence.sequence == "TTAA"


def test_parse_fasta_multiline_sequence():
    text = """>gene1
ATGC
GCTA
"""

    records = parse_fasta(text)

    assert records[0].record_id == "gene1"
    assert records[0].sequence.sequence == "ATGCGCTA"


def test_parse_fasta_sequence_before_header():
    text = """ATGC
>gene1
GCTA
"""

    with pytest.raises(ValueError):
        parse_fasta(text)


def test_read_fasta(tmp_path):
    fasta_file = tmp_path / "sample.fasta"

    fasta_file.write_text(
        ">gene1\n"
        "ATGC\n"
        ">gene2\n"
        "TTAA\n"
    )

    records = list(read_fasta(str(fasta_file)))

    assert len(records) == 2
    assert records[0].record_id == "gene1"
    assert records[0].sequence.sequence == "ATGC"
    assert records[1].record_id == "gene2"
    assert records[1].sequence.sequence == "TTAA"


def test_read_fasta_multiline(tmp_path):
    fasta_file = tmp_path / "sample.fasta"

    fasta_file.write_text(
        ">gene1\n"
        "ATGC\n"
        "GCTA\n"
    )

    records = list(read_fasta(str(fasta_file)))

    assert records[0].record_id == "gene1"
    assert records[0].sequence.sequence == "ATGCGCTA"


def test_fasta_record():
    sequence = Sequence("ATGC")

    record = FastaRecord(
        record_id="gene1",
        sequence=sequence,
        description="example gene",
    )

    assert record.record_id == "gene1"
    assert record.sequence.sequence == "ATGC"
    assert record.description == "example gene"


def test_fasta_record_empty_id():
    sequence = Sequence("ATGC")

    with pytest.raises(ValueError):
        FastaRecord("", sequence)
        
        
        
def test_sequence_length():
    dna = Sequence("ATGCGATC")

    assert dna.length == 8