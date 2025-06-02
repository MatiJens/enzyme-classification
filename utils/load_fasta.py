from Bio import SeqIO

def load_fasta(enzyme_path, not_enzyme_path, limit=10000):

    # List with enzymes sequences
    enzymes = []
    not_enzymes = []

    for enzyme, not_enzyme in zip(SeqIO.parse(enzyme_path, "fasta"), SeqIO.parse(not_enzyme_path, "fasta")):
          enzymes.append(enzyme.seq)
          not_enzymes.append(not_enzyme.seq)
          if len(not_enzymes) >= limit:
               break


    """
    # Load every sequence from fasta file and add to enzymes list
    for record in SeqIO.parse(enzyme_path, "fasta"):
            enzymes.append(record.seq)
            # Limitation of sequences number
            if len(enzymes) >= limit:
                break

    # List with not enzymes sequences
    

    # Load every sequence from fasta file and add to not enzymes list
    for record in SeqIO.parse(not_enzyme_path, "fasta"):
            not_enzymes.append(record.seq)
            # Limitation of sequences number
            if len(not_enzymes) >= limit:
                break
                """
    return enzymes, not_enzymes

