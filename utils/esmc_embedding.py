from esm.sdk.api import ESMProtein, LogitsConfig
from esm.models.esmc import ESMC
from utils import initialize_esm_client

def esmc_embedding(raw_proteins, client):

    # Transform SEQ into str
    proteins = [str(item) for item in raw_proteins]
    # List of embeddings
    embeddings = []

    for i, seq in enumerate(proteins):
        print(f"{i + 1}/{len(proteins)}")

        # Tranform sequence to correct format
        protein = ESMProtein(sequence=seq)
        # Encode sequence
        protein_tensor = client.encode(protein)
        # Create logits
        logits_output = client.logits(
            protein_tensor, LogitsConfig(return_embeddings=True)
        )
        # Save embedding to variable
        embedding = logits_output.embeddings
        # Get only first vector from embedding (global vector)
        global_embb = embedding[0, 0, :]
        # Add vector to list
        embeddings.append(global_embb)

    return embeddings