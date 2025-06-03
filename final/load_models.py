import torch
from model.MLP_enzymes import MLP_enzymes
from esm.models.esmc import ESMC

def load_models():

    client = ESMC.from_pretrained("esmc_300m").to("cpu")
    model = MLP_enzymes()
    state_dict = torch.load('model/enzymes_MLP.pth', map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)

    return client, model