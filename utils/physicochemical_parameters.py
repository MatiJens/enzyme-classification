import numpy as np
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def physicochemical_parameters(proteins):

    # List of every parameter
    ip_list = []
    mw_list = []
    gr_list = []

    for seq in proteins:
        # Transform sequence into ProteinAnalysis (it's necessary to calculate these parameters)
        seq = ProteinAnalysis(seq)

        # Calculate isoelectric point and molecular weight
        ip = seq.isoelectric_point()
        mw = seq.molecular_weight()

        # When unusual aminoacid occurs it's not possible to count gravy
        # So it's filled with nan value, then it will be filled with median
        try:
            gr = seq.gravy()
        except:
            gr = np.nan

        # Add every parameter to lists
        ip_list.append(ip)
        mw_list.append(mw)
        gr_list.append(gr)

    return ip_list, gr_list, mw_list