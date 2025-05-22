# Nei-Gojobori's method for estimating the numbers of synonymous and nonsynonymous nucleotide substitutions

# Ps. You'll have to add the nucleotides ate the beginning or end to give the algorithm the right 'pauta de lectura'


codon_code = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}


sequence = 'GATGAGATCGAGAATCTCAAGCTGGAACAGGTCCGCATGGCTCAGCAATGCGCGGACGCCCAGCGACGCGAGAAGATCCTCATGCGACGGCTGGCCAACAAGGAGCAAGAATTCCAGGACTATGTG'
n = len(sequence)
syn_positions = 0
nonsyn_positions = 0

# function compare codon's positions
def compare_codon_position(nucleotide, codon, position, codon_code, aminoacid):
    bases = ['A', 'C', 'G', 'T']
    other_bases = [base for base in bases if base != nucleotide]
    synonym, non_synonym = 0, 0
    for base in other_bases:
        new_codon = list(codon)
        new_codon[position] = base
        new_codon = ''.join(new_codon)
        if aminoacid == codon_code[new_codon]:
            synonym += 1
        else:
            non_synonym += 1
    return synonym, non_synonym

# first codon - only compare 2nd and 3rd positions
first_codon = sequence[0:3]
first_aminoacid = codon_code[first_codon]
for position in range(1,3):
    nucleotide = first_codon[position]
    synonym, non_synonym = compare_codon_position(nucleotide, first_codon, position, codon_code, first_aminoacid)
    syn_positions += (synonym / 3)
    nonsyn_positions += (non_synonym / 3)

print(syn_positions, nonsyn_positions)
for i in range(3, n, 3):
    codon = sequence[i:i+3]
    aminoacid = codon_code[codon]
    print(codon)
    for position in range(3):
        nucleotide = codon[position]
        synonym, non_synonym = compare_codon_position(nucleotide, codon, position, codon_code, aminoacid)
        syn_positions += (synonym / 3)
        nonsyn_positions += (non_synonym / 3)

print(syn_positions, nonsyn_positions)


