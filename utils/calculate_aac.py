from Bio.SeqUtils.ProtParam import ProteinAnalysis

def calculate_aac(sequence):

    # Calculate percentage of every aminoacid in sequence
    sequence = ProteinAnalysis(sequence)
    acc_percent = sequence.amino_acids_percent

    return acc_percent
