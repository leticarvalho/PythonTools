# In this file we explore BioPython library


# Sequencing & SeqIO - genomic sequences

# imported package
from Bio import SeqIO

# downloaded COVID genome from UCSC genomic browser (example)
COVID_genome = "NC_045512v2.fa"

# Fasta format:
### first line begins with a '>', and contains information about the sequence (header)
### next lines correspond to the sequence, and are maximum 80 characters

# Reading a FASTA file with SeqIO
records = SeqIO.parse(COVID_genome, "fasta")
for sequence in records:
    print(f'ID: {sequence.id}, length: {len(sequence)}')
    covid_sequence = sequence.seq

# Writing to a new FASTA file
SeqIO.write(sequence, "covid_output.fasta", "fasta")


# Counting nucleotides

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


# Calculating G-C content (Guanine-Citosine):

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

GC_content = gc_fraction(covid_sequence)*100
print(GC_content)


# Working with Seq objects
from Bio.Seq import Seq

# Sequence
seq = Seq('ATGAGTACACAGCAAGAAGTCCATACCTTATCATTTAGAGGAAGGAGAAGTCGTAACAAGGTTTCCGTAGGTGAACCCTGA')

# Its complement
comp = seq.complement()

# Its reverse complement
rev_comp = seq.reverse_complement()

# Transcribing the sequence
mRNA = seq.transcribe()
print(mRNA)

# Translating the mRNA
mRNAt = mRNA.translate()
print(mRNAt)
# The character * means that it's a stop codon


# Aligning Sequences

from Bio import Align
from Bio.Align import PairwiseAligner

aligner = PairwiseAligner()

seq1 = "GATTACA"
seq2 = "GCATGCU"

alignments = aligner.align(seq1, seq2)

best_alignment = alignments[0] # the best alignment (best score)
print(best_alignment)
print("Score:", best_alignment.score)

# Customizing the Aligner

aligner.mode = "global" # "global" or "local"
aligner.match_score = 1 # match score
aligner.mismatch_score = -1 # mismatch penalty
aligner.open_gap_score = -2 # penalty to start a new gap
aligner.extend_gap_score = -0.5 # penalty to continue an existing gap


# Codon Table

from Bio.Data import CodonTable

standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
print("Start codons:", standard_table.start_codons)
print("Stop codons:", standard_table.stop_codons)


# Sequence Annotation

from Bio.SeqFeature import SeqFeature, FeatureLocation

feature = SeqFeature(FeatureLocation(start=3, end=13), type="promoter")
print("Feature type:", feature.type)
print("Location:", feature.location)
