import torch.nn as nn

class MLP_enzymes(nn.Module):

    def __init__(self, input_len):
        
        self.input_len = input_len
        super(MLP_enzymes, self).__init__()

        self.mlp = nn.Sequential(
            nn.Linear(self.input_len, 40),
            nn.ReLU(),
            nn.Linear(40, 20),
            nn.ReLU(),
            nn.Linear(20, 10),
            nn.ReLU(),
        )

        self.fc_result = nn.Linear(10, 2)

    def forward(self, x):

        mlp_output = self.mlp(x)

        result = self.fc_result(mlp_output)

        return result