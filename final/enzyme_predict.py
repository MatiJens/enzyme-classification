import torch
from model.MLP_enzymes import MLP_enzymes
from esm.models.esmc import ESMC
from esm.sdk.api import ESMProtein, LogitsConfig
from utils.esmc_embedding import esmc_embedding

def enzyme_predict(seq, client, model):

    protein = ESMProtein(sequence=seq)
    protein_tensor = client.encode(protein)
    logits_output = client.logits(
        protein_tensor, LogitsConfig(return_embeddings=True)
    )
    embedding = logits_output.embeddings
    global_embb = embedding[0, 0, :]
    with torch.no_grad():
        predict_MLP = model(global_embb)
    predict_prob = torch.sigmoid(predict_MLP)
    predict_class = ((predict_prob > 0.5).float().squeeze()).item()

    if predict_class == 1:
        result = 'enzyme'
    else:
        result = 'not enzyme'

    return result