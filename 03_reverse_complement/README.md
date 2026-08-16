# reverse complement

beginner-friendly python project for finding the reverse complement of a dna sequence.

## what is a reverse complement?

dna has two complementary strands. each dna base pairs with another specific base:

- a → t
- t → a
- g → c
- c → g

the **complement** of a dna sequence is created by replacing each base with its matching partner.

for example:

dna:
atgc

complement:
tacg

a **reverse complement** goes one step further. after finding the complement, the sequence is reversed.

dna:
atgc

complement:
tacg

reverse complement:
gcat

this is useful because dna sequences can be read from either strand, and the reverse complement represents the corresponding sequence on the opposite strand.

## what it does

this program:

- takes a dna sequence
- checks whether it contains valid dna bases
- creates the complementary sequence
- reverses the complementary sequence
- checks that the reverse complement has the same length
- checks the result by applying the operation twice

## example

### input

atgcgatcgatgctag

### output

dna: atgcgatcgatgctag
complement: tacgctagctacgatc
reverse complement: ctagcatcgatcgcat
valid dna: true
original length: 16
reverse complement length: 16
double reverse complement: atgcgatcgatgctag
matches original: true

## why is the reverse complement important?

the reverse complement is commonly used when working with dna sequences because genes and other biological regions can occur on either strand of dna. bioinformatics programs often need to check both the original sequence and its reverse complement when searching for genes, motifs, binding sites, or other sequence patterns.

## where can this code be used?

this type of operation can be used as part of sequence analysis workflows, such as searching for a particular dna pattern on both strands, analyzing genes, studying mutations, or preparing sequences for alignment and other bioinformatics tools.

## python concepts used

- strings
- `str.translate()`
- `str.maketrans()`
- string slicing
- `[::-1]`
- `len()`
- sets
- `all()`
- boolean comparisons

## how to run

make sure python is installed, then run:

```bash
python main.py