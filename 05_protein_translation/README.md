# protein translation

python project that demonstrates how codons in a dna sequence can be translated into amino acids.

## what is protein translation?

proteins are made from smaller building blocks called amino acids. the information needed to build proteins is stored in dna.

a dna sequence can be divided into groups of three bases called codons. each codon can correspond to a specific amino acid.

for example:

dna:

ATGCGATCGATGCTAG

split into codons:

ATG | CGA | TCG | ATG | CTA

these codons can then be mapped to their corresponding amino acids.

## what it does

this program:

- takes a dna sequence
- splits it into complete codons
- maps each codon to an amino acid
- displays the resulting protein sequence
- shows each codon and its corresponding amino acid

## example

### input

ATGCGATCGATGCTAG

### output

DNA: ATGCGATCGATGCTAG
Codons: ['ATG', 'CGA', 'TCG', 'ATG', 'CTA']
Protein: ['Methionine (M)', 'Arginine (R)', 'Serine (S)', 'Methionine (M)', 'Leucine (L)']

ATG -> Methionine (M)
CGA -> Arginine (R)
TCG -> Serine (S)
ATG -> Methionine (M)
CTA -> Leucine (L)

## why is protein translation important?

protein translation is an important part of gene expression because it connects genetic information to the production of proteins. studying this process helps in understanding genes, mutations, and how changes in dna can affect proteins.

## where can this code be used?

this type of codon-to-amino-acid mapping can be used as part of a bioinformatics pipeline when analyzing coding dna sequences. it can be used as a basic step before studying the proteins produced by genes or investigating how changes in a dna sequence may affect the resulting protein.

## python concepts used

- strings
- dictionaries
- list comprehensions
- string slicing
- `range()`
- `len()`
- `zip()`
- loops

## how to run

make sure python is installed, then run:

```bash
python main.py