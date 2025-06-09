from concurrent.futures import ThreadPoolExecutor
from utils.embed_sequence import embed_sequence
from esm.sdk.api import (
    ESMProteinError
)

def batch_embed(model, inputs):
    with ThreadPoolExecutor() as executor:

        futures = [
            executor.submit(embed_sequence, model, protein) for protein in inputs
        ]

        results = []

        for future in futures:
            try:
                results.append(future.result())
            except Exception as e:
                results.append(ESMProteinError(500, str(e)))

    return results