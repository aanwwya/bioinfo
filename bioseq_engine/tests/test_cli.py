from bioseq_engine.src.bioseq.cli import main


def test_cli(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cli.py",
            "bioseq_engine/data/sample.fasta",
            "ATGC",
            "GCG",
        ],
    )

    main()

    output = capsys.readouterr().out

    assert "gene_1" in output
    assert "ATGC: [0, 5]" in output
    assert "GCG: [2, 7]" in output
    assert "gene_2" in output
    assert "gene_3" in output


def test_cli_invalid_motif(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cli.py",
            "bioseq_engine/data/sample.fasta",
            "ATGX",
        ],
    )

    try:
        main()
    except SystemExit:
        pass

    output = capsys.readouterr().err

    assert "invalid DNA bases" in output
    assert "ATGX" in output
    
def test_cli_missing_file(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "cli.py",
            "bioseq_engine/data/does_not_exist.fasta",
            "ATGC",
        ],
    )

    try:
        main()
    except SystemExit:
        pass

    output = capsys.readouterr().err

    assert "No such file or directory" in output