from Bio import SeqIO
import pandas as pd

def load_fasta(enzyme_path, not_enzyme_path, limit=1000):

    enzymes = []

    for record in SeqIO.parse(enzyme_path, "fasta"):
            enzymes.append(record.seq)
            if len(enzymes) >= limit:
                break

    not_enzymes = []

    for record in SeqIO.parse(not_enzyme_path, "fasta"):
            not_enzymes.append(record.seq)
            if len(not_enzymes) >= limit:
                break

    return enzymes, not_enzymes

