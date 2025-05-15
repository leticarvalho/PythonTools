# In this file we explore BioPython library

# PDB - proteins

# Sequencing & SeqIO - genomic sequences

# imported package
from Bio import SeqIO
# downloaded COVID genome from UCSC genomic browser
COVID_genome = "NC_045512v2.fa"

# Reading a FASTA file with SeqIO
records = SeqIO.parse(COVID_genome, "fasta")
for sequence in records:
    print(f'ID: {sequence.id}, longitud: {len(sequence)}')

# Align - sequences alignment