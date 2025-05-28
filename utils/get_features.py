import pandas as pd

from utils.calculate_aac import calculate_aac

def get_features(proteins):
    AMINO_ACIDS = 'ACDEFGHIKLMNPQRSTVWY'

    acc = [calculate_aac(seq) for seq in proteins]

    df_proteins = pd.DataFrame(acc, columns=list(AMINO_ACIDS))

    return df_proteins