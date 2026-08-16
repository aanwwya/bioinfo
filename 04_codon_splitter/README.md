# codon splitter

beginner-friendly python project for splitting a dna sequence into groups of three nucleotides called codons.

## what is a codon?

a codon is a group of three nucleotides in a dna or rna sequence. codons are important because, during protein production, groups of three bases are used to represent specific amino acids or signals.

for example:

dna:

ATGCGATCGATGCTAG

split into codons:

ATG | CGA | TCG | ATG | CTA

in this sequence, there is one extra base (`G`) at the end. since a complete codon must contain three bases, the extra base is not included as a codon.

## what it does

this program:

- takes a dna sequence
- splits it into groups of three
- identifies incomplete bases at the end
- counts the number of complete codons
- displays each codon with its position

## example

### input

ATGCGATCGATGCTAG

### output

DNA: ATGCGATCGATGCTAG
Codons: ['ATG', 'CGA', 'TCG', 'ATG', 'CTA']
Incomplete bases: 1
Number of complete codons: 5
Codon 1: ATG
Codon 2: CGA
Codon 3: TCG
Codon 4: ATG
Codon 5: CTA

## why is this important?

splitting a sequence into codons is an important step when studying how genetic information can be used to produce proteins. dividing a sequence into groups of three allows each codon to be examined individually and compared with the genetic code.

## where can this code be used?

this type of operation can be used as an early step in sequence analysis before translating a coding DNA or RNA sequence into a protein. it can also be useful when studying genes, identifying coding regions, analyzing mutations, and building larger bioinformatics pipelines.

## python concepts used

- strings
- list comprehensions
- `range()`
- `len()`
- `enumerate()`
- string slicing
- modulo `%`
- lists

## how to run

make sure python is installed, then run:

```bash
python main.py