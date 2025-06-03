import torch
import torch.nn as nn

class MLP_enzymes(nn.Module):

    def __init__(self):
        
        super(MLP_enzymes, self).__init__()

        self.mlp = nn.Sequential(
            nn.Linear(960, 1024),
            nn.ReLU(),
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
        )

        self.fc_result = nn.Linear(256, 1)

    def forward(self, x):

        mlp_output = self.mlp(x)

        result = self.fc_result(mlp_output)

        return result