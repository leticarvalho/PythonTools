# In this file we explore some of the basic libraries in Python

import os

file_name = ''
nucleotides = {}
with open(file_name) as file:
    lines = file.read().split(os.linesep)
    for line in lines:
        if line.startswith('>'):
            nucleotides[organism] = organism_nucleotides
            organism = line[:]
            organism_nucleotides = {
                "A": 0,
                "C": 0,
                "G": 0,
                "T": 0
            }
        else:
            for nucleotide in line:
                organism_nucleotides[nucleotide] += 1