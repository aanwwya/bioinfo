import argparse

from bioseq_engine.src.bioseq.engine import BioSequenceEngine


def main():
    parser = argparse.ArgumentParser(
        description="Search DNA sequences for multiple motifs."
    )

    parser.add_argument(
        "fasta",
        help="path to the FASTA file",
    )

    parser.add_argument(
        "motifs",
        nargs="+",
        help="DNA motifs to search for",
    )

    args = parser.parse_args()

    try:
        engine = BioSequenceEngine(args.motifs)
        results = engine.search_file(args.fasta)

    except (ValueError, FileNotFoundError) as error:
        parser.error(str(error))

    for record_id, matches in results.items():
        print(f"\n{record_id}")

        for motif, positions in matches.items():
            print(f"  {motif}: {positions}")


if __name__ == "__main__":
    main()