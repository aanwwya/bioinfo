from bioseq_engine.src.bioseq.engine import BioSequenceEngine


def test_search_file():
    engine = BioSequenceEngine(["ATGC", "GCG"])

    results = engine.search_file(
        "bioseq_engine/data/sample.fasta"
    )

    assert results["gene_1"]["ATGC"] == [0, 5]
    assert results["gene_1"]["GCG"] == [2, 7]