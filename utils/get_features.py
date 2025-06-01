import pandas as pd
from sklearn.preprocessing import StandardScaler

from utils.calculate_aac import calculate_aac
from utils.physicochemical_parameters import physicochemical_parameters

def get_features(proteins):

    # Count percentage of every aminoacid in sequence
    df_proteins = pd.DataFrame([calculate_aac(seq) for seq in proteins])

    # Calculate isoelectric point, gravy and molecular weight
    ip, gr, mw = physicochemical_parameters(proteins)

    # Add new columns with features
    df_proteins['gravy'] = gr
    #df_proteins['mw'] = mw
    #df_proteins['ip'] = ip

    # Fill nan gravy with median value
    gravy_median = df_proteins['gravy'].median()
    df_proteins.fillna({'gravy' :gravy_median}, inplace=True)

    #mw_median = df_proteins['mw'].median()
    #df_proteins.fillna({'mw' :mw_median}, inplace=True)

    #ip_median = df_proteins['ip'].median()
    #df_proteins.fillna({'ip' :gravy_median}, inplace=True)

    useless_aac = ['L', 'N', 'K', 'A', 'T', 'M']
    df_proteins = df_proteins.drop(columns=useless_aac)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(df_proteins)

    df_scaled = pd.DataFrame(scaled, columns=df_proteins.columns)

    return df_proteins