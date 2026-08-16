# dna sequence analyzer

beginner-friendly python project for performing basic dna sequence analysis.

## what it does

this program analyzes a dna sequence and calculates:

- dna sequence length
- number of a, t, g, and c nucleotides
- gc content
- at content
- whether the sequence contains only valid dna bases
- complementary dna sequence

## example

### input

atgcgatcgatgctag

### output

dna: atgcgatcgatgctag  
length: 16  
counts: counter({'g': 5, 'a': 4, 't': 4, 'c': 3})  
gc content: 50.0 %  
valid dna: true  
at content: 50.0 %  
complement: tacgctagctacgatc

## python concepts used

- strings
- `len()`
- `counter` from the `collections` module
- sets
- `all()`
- string translation using `str.translate()`
- basic mathematical calculations

## biology concepts

dna is composed of four nucleotide bases:

- a — adenine
- t — thymine
- g — guanine
- c — cytosine

gc content represents the percentage of g and c bases in a dna sequence.

the complementary bases are:

- a → t
- t → a
- g → c
- c → g

## why is dna sequence analysis important?

dna sequence analysis helps us understand the composition and basic patterns of dna. it can be used to check the length and nucleotide composition of a sequence, calculate gc content, verify valid dna bases, and generate its complementary strand. these basic steps are often used before further analysis in bioinformatics, genetics, genomics, and medical research.

## how to run

make sure python is installed, then run:

```bash
python main.py