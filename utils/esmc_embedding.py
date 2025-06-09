from esm.sdk.api import (
    ESM3InferenceClient,
    ESMProtein,
    ESMProteinError,
    LogitsConfig,
    LogitsOutput,
    ProteinType,
)
from concurrent.futures import ThreadPoolExecutor
import torch

def esmc_embedding(data, client, batch_size=32):

    # Convert sequences to ESMProtein objects
    proteins = [ESMProtein(sequence=str(seq)) for seq in data['sequence']]
    num_proteins = len(proteins)
    # List of embeddings
    all_embeddings = []

    for i in range(0, num_proteins, batch_size):
        # Create batch of proteins
        batch = proteins[i:i + batch_size]
        print(f"Batch {i//batch_size}/{num_proteins//batch_size}")

        # Encode every protein in batch
        encoded_proteins = [client.encode(p) for p in batch]

        # Transform ESMProteinTensor to tensor
        list_of_tensors = [encoded_p.tensor() for encoded_p in encoded_proteins]

        # Create tensor from list of encoded proteins
        protein_tensor = torch.cat(list_of_tensors, dim=0)

        # Create logits
        logits_output = client.logits(
            protein_tensor, LogitsConfig(return_embeddings=True)
        )

        # Get only first vector from embedding (global vector)
        embeddings_batch = logits_output.embeddings[:, 0, :]

        # Add new embeddings to list of all embeddings
        all_embeddings.extend(embeddings_batch.detach())

    # Add embeddings as new feature to df
    data['embeddings'] = [emb.numpy() for emb in all_embeddings]

    # Remove sequence column it's unnecessary now
    data = data.drop(columns=['sequence'])

    return data