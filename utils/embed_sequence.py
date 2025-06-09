from esm.sdk.api import (
    ESMProtein,
    LogitsConfig
)

def embed_sequence(model, sequence):
    protein = ESMProtein(sequence=sequence)
    protein_tensor = model.encode(protein)
    
    EMBEDDING_CONFIG = LogitsConfig(
        return_embeddings=True
    )

    logits = model.logits(protein_tensor, EMBEDDING_CONFIG)

    output = logits.embeddings[0, 0, :]

    return output