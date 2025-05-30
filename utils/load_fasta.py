from Bio import SeqIO

def load_fasta(enzyme_path, not_enzyme_path, limit=1000):

    # List with enzymes sequences
    enzymes = []

    # Load every sequence from fasta file and add to enzymes list
    for record in SeqIO.parse(enzyme_path, "fasta"):
            enzymes.append(record.seq)
            # Limitation of sequences number
            if len(enzymes) >= limit:
                break

    # List with not enzymes sequences
    not_enzymes = []

    # Load every sequence from fasta file and add to not enzymes list
    for record in SeqIO.parse(not_enzyme_path, "fasta"):
            not_enzymes.append(record.seq)
            # Limitation of sequences number
            if len(not_enzymes) >= limit:
                break

    return enzymes, not_enzymes

