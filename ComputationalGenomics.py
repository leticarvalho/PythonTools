# Adapting a GFF file

import os

gff_geneid = """
chr21	exon	first	157	286	500	+	0	GEN1
chr21	exon	internal	10376	10458	500	+	2	GEN1
chr21	exon	internal	12800	12857	500	+	0	GEN1
chr21	exon	internal	15504	15655	500	+	2	GEN1
chr21	exon	internal	16764	16828	500	+	0	GEN1
chr21	exon	internal	17225	17406	500	+	1	GEN1
chr21	exon	internal	23771	23865	500	+	2	GEN1
chr21	exon	internal	25045	25142	500	+	0	GEN1
chr21	exon	internal	26262	26281	500	+	1	GEN1
chr21	exon	internal	27296	27427	500	+	2	GEN1
chr21	exon	terminal	28008	28858	500	+	2	GEN1
chr21	exon	first	30518	30529	500	+	0	GEN2
chr21	exon	internal	30780	30932	500	+	0	GEN2
chr21	exon	internal	31931	31994	500	+	0	GEN2
chr21	exon	terminal	33682	33875	500	+	2	GEN2"""

gff_genescan = """
chr21	exon	first	157	286	500	+	0	GEN
chr21	exon	internal	10376	10458	500	+	0	GEN
chr21	exon	internal	12800	12857	500	+	1	GEN
chr21	exon	internal	14362	14447	500	+	2	GEN
chr21	exon	internal	15128	15189	500	+	1	GEN
chr21	exon	internal	15526	15655	500	+	1	GEN
chr21	exon	internal	16764	16828	500	+	2	GEN
chr21	exon	internal	17225	17406	500	+	2	GEN
chr21	exon	internal	23771	23865	500	+	0	GEN
chr21	exon	internal	25045	25142	500	+	0	GEN
chr21	exon	internal	26262	26281	500	+	0	GEN
chr21	exon	internal	27296	27427	500	+	0	GEN
chr21	exon	internal	27663	27851	500	+	1	GEN
chr21	exon	internal	28008	28732	500	+	1	GEN
chr21	exon	internal	30236	30380	500	+	1	GEN
chr21	exon	internal	30589	30671	500	+	2	GEN
chr21	exon	internal	30780	30932	500	+	2	GEN
chr21	exon	internal	31931	31994	500	+	1	GEN
chr21	exon	terminal	33682	33875	500	+	2	GEN
"""

gff_fgenesh = """
chr21	exon	first	157	286	500	+	0	GEN
chr21	exon	internal	10376	10458	500	+	1	GEN
chr21	exon	internal	12800	12857	500	+	1	GEN
chr21	exon	internal	14362	14447	500	+	1	GEN
chr21	exon	internal	15128	15189	500	+	1	GEN
chr21	exon	internal	15526	15655	500	+	1	GEN
chr21	exon	internal	16764	16828	500	+	1	GEN
chr21	exon	internal	17225	17406	500	+	1	GEN
chr21	exon	internal	23771	23865	500	+	1	GEN
chr21	exon	internal	25045	25142	500	+	1	GEN
chr21	exon	internal	26262	26281	500	+	1	GEN
chr21	exon	internal	27296	27427	500	+	1	GEN
chr21	exon	internal	28008	28732	500	+	1	GEN
chr21	exon	internal	30780	30932	500	+	1	GEN
chr21	exon	internal	31931	31994	500	+	1	GEN
chr21	exon	terminal	33682	33875	500	+	1	GEN
"""

number = 43659560

def add_position_gff(gff_string, add_number):
    lines = [line for line in gff_string.split("\n") if line != '']
    new_lines = []
    for line in lines:
        columns = line.split("\t")
        columns[3] = str(int(columns[3]) + add_number)
        columns[4] = str(int(columns[4]) + add_number)
        new_lines.append("\t".join(columns))
    return "\n".join(new_lines)

print(add_position_gff(gff_geneid, number), "\n\n")
print(add_position_gff(gff_genescan, number), "\n\n")
print(add_position_gff(gff_fgenesh, number), "\n\n")
