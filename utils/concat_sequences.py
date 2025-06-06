import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import torch


def concat_sequences(enzyme, not_enzyme, ready_data_path):

    # Concat enzymes and not enzymes embeddings
    all_embeddings = torch.stack(enzyme + not_enzyme).cpu().numpy()

    # Create labels for every sequence
    labels = np.array([1] * len(enzyme) + [0] * len(not_enzyme))
    
    # Create df of all embeddings
    proteins = pd.DataFrame(all_embeddings)

    # Add target value
    proteins['labels'] = labels

    # Save data to csv
    proteins.to_csv(ready_data_path, index=False)

    return proteins
