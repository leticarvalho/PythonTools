# In this file we explore BioPython library

# PDB - proteins

# Sequencing & SeqIO - genomic sequences

# imported package
from Bio import SeqIO
# downloaded COVID genome from UCSC genomic browser
COVID_genome = "NC_045512v2.fa"

# Fasta format:
### first line begins with a '>', and contains information about the sequence (header)
### next lines correspond to the sequence, and are maximum 80 characters

# Reading a FASTA file with SeqIO
records = SeqIO.parse(COVID_genome, "fasta")
for sequence in records:
    print(f'ID: {sequence.id}, longitud: {len(sequence)}')

# Count nucleotides

def counting_nucleotides(fasta_file, organism=''):
    """
    :param fasta_file: file in fasta format
    :param organism: organism to select in a multifasta file (default = all)
    :return: nucleotides percentages
    """
    records = SeqIO.parse(fasta_file, "fasta")
    nucleotides = {}
    for seq_record in records:
        if organism.lower() in seq_record.description.lower():
            seq_length = len(seq_record.seq)
            nucleotides[seq_record.id] = {
                "A": round((seq_record.seq.count("A") / seq_length) * 100, 1),
                "C": round((seq_record.seq.count("C") / seq_length) * 100, 1),
                "G": round((seq_record.seq.count("G") / seq_length) * 100, 1),
                "T": round((seq_record.seq.count("T") / seq_length) * 100, 1)
            }
    return nucleotides

print(counting_nucleotides(COVID_genome))

# Align - sequences alignment