import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch import optim

def train_mlp(model, x_train, y_train):

    y_train_reshaped = y_train.float().unsqueeze(1)

    #HIPERPARAMETERS
    EPOCHS = 1000
    LR = 0.0012
    LOSS_BREAK = 0.08

    # Create criterion and optimizer
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=LR)

    # List of loss of every epoch
    loss_per_epoch = []

    for epoch in range(EPOCHS):

        # Model training
        model.train()
        outputs = model(x_train)
        loss = criterion(outputs, y_train_reshaped)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Add current loss to list
        loss_per_epoch.append(loss.item())

        #Print current loss every 20 epochs
        if(epoch + 1) % 20 == 0:
            print(f"Epoch {epoch + 1}/{EPOCHS}, Loss {loss.item():.4f}")
        
        if loss.item() < LOSS_BREAK:
            print(f"{LOSS_BREAK} achieved, stopping learning process")
            break 

    plt.plot(loss_per_epoch)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Loss per epoch')