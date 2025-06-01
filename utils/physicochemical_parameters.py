import numpy as np
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def physicochemical_parameters(proteins):

    # List of every parameter
    mw_list = []
    gr_list = []
    ip_list = []

    for seq in proteins:
        # Transform sequence into ProteinAnalysis (it's necessary to calculate these parameters)
        seq = ProteinAnalysis(seq)     

        # When unusual aminoacid occurs it's not possible to count gravy
        # So it's filled with nan value, then it will be filled with median
        try:
            gr = seq.gravy()
        except:
            gr = np.nan

        try:
            mw = seq.molecular_weight()
        except:
            mw = np.nan

        try:
            ip = seq.isoelectric_point()
        except:
            ip = np.nan

        # Add every parameter to lists
        mw_list.append(mw)
        gr_list.append(gr)
        ip_list.append(ip)

    return ip_list, gr_list, mw_list