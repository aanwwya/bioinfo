# dna transcription

beginner-friendly python project that demonstrates how a dna sequence can be transcribed into rna.

## what is transcription?

transcription is the process of making an rna copy from a dna sequence. dna stores genetic information, while rna can carry this information so it can be used by the cell to make proteins.

during transcription, the dna bases are copied into an rna sequence. rna uses **u (uracil)** instead of **t (thymine)**, so in this simplified program:

- a → a
- t → u
- g → g
- c → c

for example:

dna:
atgcgatcgatgctag

rna:
augcgaucgaugcuag

## what it does

this program:

- takes a dna sequence
- checks whether it contains valid dna bases
- converts the dna sequence into rna
- checks whether the resulting rna contains valid rna bases
- compares the number of t bases in dna with u bases in rna
- checks that the sequence length remains the same

## example

### input

atgcgatcgatgctag

### output

dna: atgcgatcgatgctag
rna: augcgaucgaugcuag
valid dna: true
rna length: 16
valid rna: true
t in dna: 4
u in rna: 4

## why is transcription important?

transcription is an important step in gene expression because it allows information stored in dna to be copied into rna. this rna can then be used in later processes involved in protein production. understanding transcription is therefore important when studying genes, genetic disorders, molecular biology, and bioinformatics.

## where can this code be used?

a simple transcription program can be useful when working with dna sequences in bioinformatics. for example, a researcher could use it to convert a dna sequence into an rna sequence before studying rna sequences, identifying coding regions, or performing further computational analysis.

## python concepts used

- strings
- `replace()`
- `len()`
- `count()`
- sets
- `all()`

## how to run

make sure python is installed, then run:

```bash
python main.py