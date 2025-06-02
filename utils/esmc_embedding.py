from esm.sdk.api import ESMProtein, LogitsConfig

from utils import initialize_esm_client

def esmc_embedding(seq):

    global _client
    if _client is None:
        initialize_esm_client()

    protein = ESMProtein(sequence=seq)
    protein_tensor = _client.encode(protein)
    logits_output = _client.logits(
        protein_tensor, LogitsConfig(sequence=True, return_embeddings=True)
    )

    return logits_output.embeddings