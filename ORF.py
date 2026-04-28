dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

Udna = dna.replace("T", "U")

table = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}


orf1 = [Udna[i : i + 3] for i in range(0, len(Udna), 3)]
orf2 = [Udna[i : i + 3] for i in range(1, len(Udna), 3)]
orf3 = [Udna[i : i + 3] for i in range(2, len(Udna), 3)]
# print(f"{Udna=}")

orfs = [orf1, orf2, orf3]
aa1 = "".join([table[c] for c in orf1 if len(c) == 3])
stop_splits = aa1.split("Stop")
print(stop_splits)

print(aa1)

# for orf in orfs:
#     aa = "".join([table[c] for c in orf if len(c) == 3])
#     print(aa)


rev = Udna[::-1]
revdna = rev.translate(str.maketrans("AUCG", "UAGC"))


# print(f"{revdna=}")

rorf1 = [revdna[i : i + 3] for i in range(0, len(revdna), 3)]
rorf2 = [revdna[i : i + 3] for i in range(1, len(revdna), 3)]
rorf3 = [revdna[i : i + 3] for i in range(2, len(revdna), 3)]
