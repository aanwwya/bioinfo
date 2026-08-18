# bioseq engine

a small bioinformatics sequence-analysis engine built from scratch in python.

## what it does

bioseq engine can:

* parse dna sequences from fasta files
* validate dna sequences
* calculate nucleotide composition
* calculate gc content
* find the shortest and longest sequences in a dataset
* search for dna motifs
* find overlapping motif matches
* search for multiple motifs efficiently
* compare different string-search algorithms
* provide a command-line interface

## algorithms

the project implements three approaches to sequence searching.

### naive search

checks every possible position in the sequence and compares the pattern directly.

simple to understand, but becomes slower as the sequence and number of searches grow.

### kmp

**knuth-morris-pratt**

uses a longest-prefix-suffix (lps) table to avoid repeating unnecessary comparisons.

useful when searching for a single motif efficiently.

### aho-corasick

builds a trie containing multiple motifs and adds failure links between nodes.

this allows multiple motifs to be searched simultaneously in a single pass through the sequence.

this is especially useful when working with many motifs.

## benchmark

the project includes benchmarks comparing kmp against aho-corasick when searching for increasing numbers of motifs.

| motifs | kmp (s) | aho-corasick (s) | speedup |
| -----: | ------: | ---------------: | ------: |
|      8 |    3.47 |             0.94 |   3.69x |
|     16 |    6.32 |             1.20 |   5.27x |
|     32 |   12.33 |             1.21 |  10.16x |
|     64 |   20.68 |             1.31 |  15.82x |
|    128 |   41.20 |             1.53 |  26.97x |

as the number of motifs increases, aho-corasick becomes substantially faster than running kmp separately for every motif.

## project structure

```text
bioseq_engine/
│
├── benchmarks/
│   ├── aho_corasick_benchmark.py
│   ├── benchmark_search.py
│   ├── comparison.py
│   ├── kmp_benchmark.py
│   ├── motif_benchmark.py
│   └── run_comparison.py
│
├── data/
│   └── sample.fasta
│
├── docs/
│
├── examples/
│
├── src/
│   └── bioseq/
│       ├── analysis.py
│       ├── cli.py
│       ├── dataset.py
│       ├── engine.py
│       ├── fasta.py
│       ├── fasta_record.py
│       ├── kmp.py
│       ├── search.py
│       ├── sequence.py
│       ├── trie.py
│       └── validation.py
│
├── tests/
│   ├── test_cli.py
│   ├── test_dataset.py
│   ├── test_engine.py
│   ├── test_search.py
│   ├── test_sequence.py
│   └── test_trie.py
│
├── pyproject.toml
└── README.md
```

## usage

install the package in editable mode:

```bash
pip install -e .
```

then search a fasta file for one or more motifs:

```bash
bioseq data/sample.fasta ATGC GCG
```

example output:

```text
gene_1
  ATGC: [0, 5]
  GCG: [2, 7]

gene_2
  ATGC: [2, 9]
  GCG: [4, 6, 11]

gene_3
  ATGC: [7]
  GCG: [0, 9, 11, 13]
```

the positions represent the zero-based index where each motif starts.

## python api

the engine can also be used directly from python:

```python
from bioseq_engine.src.bioseq.engine import BioSequenceEngine

engine = BioSequenceEngine(["ATGC", "GCG"])

results = engine.search_file(
    "data/sample.fasta"
)

print(results)
```

## fasta support

bioseq engine supports standard fasta-style records:

```text
>gene_1
ATGCGATGC

>gene_2
GGCATGCG
```

sequences can span multiple lines and are combined into a single sequence during parsing.

## testing

the project uses pytest.

run the complete test suite with:

```bash
python -m pytest -v
```

current test status:

```text
46 passed
```

the tests cover:

* sequence validation
* sequence indexing and slicing
* sequence iteration
* nucleotide composition
* gc content
* naive search
* kmp search
* lps construction
* fasta parsing
* fasta file reading
* dataset statistics
* motif searching
* trie construction
* failure links
* overlapping motif matches
* cli behaviour
* invalid input handling
* missing files

## design goals

the project was built to focus on understanding the underlying algorithms rather than relying on existing bioinformatics libraries.

the main goals are:

* implement core sequence operations from scratch
* understand string-search algorithms
* handle real fasta input
* build reusable python components
* test each component independently
* measure algorithm performance
* expose the functionality through a simple cli

## status

the core engine is complete and fully tested.

```text
46 tests passed
```

the project currently supports dna sequence analysis, fasta parsing, single and multi-motif searching, algorithm benchmarking, and a packaged command-line interface.
