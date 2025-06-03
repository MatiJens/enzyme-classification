from Bio import SeqIO

def load_fasta(enzyme_path, not_enzyme_path, limit=10000):

    # List with enzymes/not enzymes sequences
    enzymes = []
    not_enzymes = []

    # Add every sequence to lists from FASTA file using biopython
    for enzyme, not_enzyme in zip(SeqIO.parse(enzyme_path, "fasta"), SeqIO.parse(not_enzyme_path, "fasta")):
          enzymes.append(enzyme.seq)
          not_enzymes.append(not_enzyme.seq)
          if len(not_enzymes) >= limit:
               break
          
    return enzymes, not_enzymes

