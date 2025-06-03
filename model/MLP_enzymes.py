import torch
import torch.nn as nn

class MLP_enzymes(nn.Module):

    def __init__(self):
        
        super(MLP_enzymes, self).__init__()

        # Input and hidden layers, Input have 960 neurons - it's length of embedding vector
        self.mlp = nn.Sequential(
            nn.Linear(960, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
        )

        # Output layer, 1 neuron because it will predict TRUE/FALSE
        self.fc_result = nn.Linear(256, 1)

    def forward(self, x):

        mlp_output = self.mlp(x)
        result = self.fc_result(mlp_output)
        return result