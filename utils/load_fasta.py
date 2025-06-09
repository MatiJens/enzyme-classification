from Bio import SeqIO
import os
import pandas as pd

def load_fasta(path, seq_limit, list_limit):

    # List with all sequences
    all_sequences = []
    # Load every type of enzyme (0 = not enzyme)
    for i in range(8):
        ec_sequences = []
        file_path = os.path.join(path, f"EC{i}.fasta")

        # Check if file exists
        try:
            iterator = SeqIO.parse(file_path, "fasta")
        except FileNotFoundError:
            print(f"Not found {file_path}, skipping it")
            continue
        
        # Load sequences from fasta file and count number of sequences
        for record in iterator:
            # If limit is reached leave the loop
            if len(ec_sequences) >= list_limit:
                break
            # Create new dictionary and add it to list
            if seq_limit >= len(str(record.seq)) > 25:
                new_sequence = {'sequence' : str(record.seq), 'EC' : i}
                ec_sequences.append(new_sequence)
        
        all_sequences.extend(ec_sequences)

    # Create df with all loaded data
    data = pd.DataFrame(all_sequences)
    return data
