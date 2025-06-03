import torch
from model.MLP_enzymes import MLP_enzymes
from esm.models.esmc import ESMC
from esm.sdk.api import ESMProtein, LogitsConfig
from utils.esmc_embedding import esmc_embedding

def enzyme_predict(seq, client, model):

    # Encode sequence
    protein = ESMProtein(sequence=seq)
    protein_tensor = client.encode(protein)
    # Create logit of it
    logits_output = client.logits(
        protein_tensor, LogitsConfig(return_embeddings=True)
    )
    # Extract embedding
    embedding = logits_output.embeddings
    # Extract global embedding vector
    global_embb = embedding[0, 0, :]
    with torch.no_grad():
        # Use model to predict enzyme/not enzyme
        predict_MLP = model(global_embb)
    # Calculate the prediction
    predict_prob = torch.sigmoid(predict_MLP)
    predict_class = ((predict_prob > 0.5).float().squeeze()).item()

    if predict_class == 1:
        probability = predict_prob.item()
        result = 'enzyme'
    else:
        result = 'not enzyme'
        probability = 1 - predict_prob.item()

    return result, probability