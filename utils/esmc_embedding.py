from esm.sdk.api import ESMProtein, LogitsConfig
from esm.models.esmc import ESMC
from utils import initialize_esm_client

def esmc_embedding(raw_proteins, client):

    proteins = [str(item) for item in raw_proteins]
    embeddings = []

    for i, seq in enumerate(proteins):
        print(f"{i + 1}/{len(proteins)}")
        protein = ESMProtein(sequence=seq)
        protein_tensor = client.encode(protein)
        logits_output = client.logits(
            protein_tensor, LogitsConfig(return_embeddings=True)
        )
        embedding = logits_output.embeddings
        global_embb = embedding[0, 0, :]
        embeddings.append(global_embb)

    return embeddings