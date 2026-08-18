# bioseq engine

a small dna sequence analysis engine written in python.

i built this project from scratch to understand how common sequence analysis and pattern matching tools work internally. it can read fasta files, validate dna sequences, calculate basic sequence statistics, and search for dna motifs.

the search side of the project includes naive search, kmp, and aho corasick, with benchmarks to compare how they behave as the number of motifs increases.

## about

bioseq engine is built around a simple idea: take a collection of dna sequences and make it easy to inspect and search them.

the project handles things like:

• dna validation
• fasta parsing
• nucleotide composition
• gc content
• sequence statistics
• single motif searching
• multiple motif searching
• overlapping matches
• kmp pattern matching
• aho corasick pattern matching
• command line usage
• performance benchmarking

the main focus of the project is the search engine. instead of using an existing pattern matching library, the algorithms are implemented directly in python.

## performance results

the main benchmark compares kmp against aho corasick while increasing the number of motifs.

| motifs |     kmp | aho corasick | speedup |
| -----: | ------: | -----------: | ------: |
|      8 |  3.47 s |       0.94 s |   3.69x |
|     16 |  6.32 s |       1.20 s |   5.27x |
|     32 | 12.33 s |       1.21 s |  10.16x |
|     64 | 20.68 s |       1.31 s |  15.82x |
|    128 | 41.20 s |       1.53 s |  26.97x |

the difference becomes much larger as the number of motifs increases.

with kmp, each motif is searched separately. aho corasick builds one search structure containing all the motifs and then scans the sequence once.

for this benchmark, that made aho corasick significantly faster when searching many motifs.

these numbers are specific to the benchmark setup and can change depending on the machine, sequence size, and motifs being tested.

## consolidated benchmark results

| algorithm    | best use case                     | approach                                                         |
| ------------ | --------------------------------- | ---------------------------------------------------------------- |
| naive search | simple or small searches          | checks every possible starting position                          |
| kmp          | searching one pattern efficiently | uses an lps table to skip unnecessary comparisons                |
| aho corasick | searching many patterns           | uses a trie and failure links to search multiple motifs together |

the general pattern from the benchmarks is:

```text
few motifs
    |
    v
kmp is simple and effective

many motifs
    |
    v
aho corasick becomes more useful
```

## quick start

clone the repository:

```bash
git clone https://github.com/aanwwya/bioinfo.git
cd bioinfo/bioseq_engine
```

install the package:

```bash
python -m pip install -e .
```

run the tests:

```bash
python -m pytest -v
```

current test suite:

```text
46 passed
```

you can also check that the installed package works:

```bash
python -c "import bioseq_engine; print('bioseq engine import successful')"
```

## architecture

```text
                       fasta file
                           |
                           v
                    +--------------+
                    | fasta parser |
                    +--------------+
                           |
                           v
                    +--------------+
                    | fastarecord  |
                    +--------------+
                           |
                           v
                    +--------------+
                    |   sequence   |
                    +--------------+
                           |
              +------------+------------+
              |                         |
              v                         v
       sequence analysis           motif search
              |                         |
              |              +----------+----------+
              |              |          |          |
              |              v          v          v
              |           naive       kmp    aho corasick
              |                                  |
              |                           +------+------+
              |                           | trie       |
              |                           | failure    |
              |                           | links      |
              |                           +------+------+
              |                                  |
              +----------------+-----------------+
                               |
                               v
                         search results
                               |
                    +----------+----------+
                    |                     |
                    v                     v
                   cli                   api
```

## usage

the project provides a command line tool called `bioseq`.

from inside the `bioseq_engine` directory:

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

the positions are zero based indexes.

the cli accepts one or more motifs:

```bash
bioseq data/sample.fasta ATGC
```

or:

```bash
bioseq data/sample.fasta ATGC GCG TATA
```

it also handles invalid input.

for example:

```bash
bioseq data/sample.fasta ATGX
```

will reject the motif because `x` is not a valid dna base.

missing fasta files are also reported instead of causing an unhandled python traceback.

## run benchmarks

all benchmark scripts are inside `benchmarks/`.

run the main comparison with:

```bash
python benchmarks/run_comparison.py
```

there are separate benchmark files for the different search approaches:

```text
benchmarks/
├── aho_corasick_benchmark.py
├── comparison.py
├── kmp_benchmark.py
├── motif_benchmark.py
└── run_comparison.py
```

the benchmark setup can be changed to experiment with different numbers of motifs and sequence sizes.

## language baseline

the project is written in python.

python was used because it makes it easier to focus on the algorithms and data structures without adding unnecessary complexity around the implementation.

the core search algorithms do not depend on external bioinformatics libraries.

the main external development dependency is `pytest`, which is used for testing.

## api

the package can also be used directly from python instead of the cli.

for example, creating and analysing a sequence:

```python
from bioseq_engine.src.bioseq.sequence import Sequence
from bioseq_engine.src.bioseq.analysis import gc_content

dna = Sequence("ATGCGATC")

print(dna.length)
print(gc_content(dna))
```

motif searching:

```python
from bioseq_engine.src.bioseq.search import MotifSearchEngine

engine = MotifSearchEngine(["ATGC", "GCG"])

results = engine.search_dataset(records)
```

the project also exposes functionality for:

• fasta parsing
• sequence validation
• nucleotide composition
• gc content
• dataset statistics
• longest and shortest records
• kmp searching
• trie construction
• aho corasick searching

## project structure

```text
bioseq_engine/
|
├── benchmarks/
│   ├── aho_corasick_benchmark.py
│   ├── comparison.py
│   ├── kmp_benchmark.py
│   ├── motif_benchmark.py
│   └── run_comparison.py
|
├── data/
│   └── sample.fasta
|
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
|
├── tests/
│   ├── test_cli.py
│   ├── test_dataset.py
│   ├── test_engine.py
│   ├── test_search.py
│   ├── test_sequence.py
│   └── test_trie.py
|
├── pyproject.toml
├── readme.md
├── license
└── .gitignore
```

## technical details

### sequence

the `sequence` class represents a dna sequence and handles basic validation and sequence operations.

it supports:

```python
dna[0]
dna[2:6]
len(dna)
list(dna)
```

slicing returns another `sequence` object.

### fasta

the fasta parser supports multiple records and sequences split across multiple lines.

for example:

```text
>gene_1
ATGC
GCTA
```

is read as one sequence:

```text
ATGCGCTA
```

each record is represented using `fastarecord`.

### sequence analysis

the analysis module currently provides nucleotide composition and gc content.

for example:

```text
a = 2
c = 2
g = 2
t = 2
```

gc content is calculated as:

```text
(g + c) / total bases × 100
```

### kmp

kmp uses a longest prefix suffix table to avoid repeating comparisons that have already been made.

the project includes both the lps construction and the actual kmp search implementation.

it also tests kmp against the naive implementation to make sure both approaches return the same matches.

### aho corasick

the aho corasick implementation is used when multiple motifs need to be searched.

the motifs are first inserted into a trie.

failure links are then created between nodes.

the resulting automaton can process a sequence in one pass and report matches for multiple motifs, including overlapping matches.

this is the main reason it performs better than running kmp separately for every motif when the motif count becomes large.

## testing

the project currently has 46 tests.

they cover:

• sequence creation and validation
• indexing and slicing
• sequence iteration
• nucleotide composition
• gc content
• fasta parsing
• multiline fasta records
• dataset statistics
• longest and shortest records
• motif searching
• kmp
• trie construction
• failure links
• overlapping matches
• aho corasick searching
• cli behaviour
• missing files
• invalid motifs

run everything with:

```bash
python -m pytest -v
```

## requirements

python 3.12 or newer is recommended.

install the project:

```bash
python -m pip install -e .
```

install pytest if it is not already available:

```bash
pip install pytest
```

no external bioinformatics framework is required for the core functionality.

## limitations

the current version focuses on standard dna sequences using:

```text
a c g t
```

it does not currently handle the full range of biological sequence formats or ambiguity codes.

the benchmark numbers are also dependent on the machine and dataset used.

## license

this project is licensed under the mit license.

see the `license` file for the full license text.
