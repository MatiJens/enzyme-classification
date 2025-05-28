def calculate_aac(sequence):
    AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'

    acc = []
    for aminoacid in AMINO_ACIDS:
        acc.append(sequence.count(aminoacid) / len(sequence))

    return acc
