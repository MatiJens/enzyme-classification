import pandas as pd

from utils.calculate_aac import calculate_aac
from utils.physicochemical_parameters import physicochemical_parameters

def get_features(proteins):

    # Count percentage of every aminoacid in sequence
    df_proteins = pd.DataFrame([calculate_aac(seq) for seq in proteins])

    # Calculate isoelectric point, gravy and molecular weight
    ip, gr, mw = physicochemical_parameters(proteins)

    # Add new columns with features
    df_proteins['ip'] = ip
    df_proteins['gravy'] = gr
    df_proteins['molecular weight'] = mw

    # Fill nan gravy with median value
    gravy_median = df_proteins['gravy'].median()
    df_proteins.fillna({'gravy' :gravy_median}, inplace=True)

    return df_proteins