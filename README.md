# Enzyme Classification

## Description:
A machine learning project for binary classification of protein sequences as enzymes or non-enzymes using ESM-C embeddings and neural networks.

Technologies Used:
-  **ESM-C**: Protein language model for generating sequence embeddings
-  **PyTorch**: Deep learning framework for MLP implementation
-  **scikit-learn**: Random Forest classifier and evaluation metrics
-  **BioPython**: FASTA file processing
-  **Tkinter**: GUI for end-user predictions

## Installation:
  Clone the repository:
  ```bash
    git clone https://github.com/MatiJens/enzyme-classification.git
    cd enzyme-classification
  ```

  Create virtual environment:
  ```bash
    python -m venv enzyme_env
    source enzyme_env/bin/activate
  ```
  Install dependencies:
  ```bash
    pip install -r requirements.txt
  ```

## Dataset:
-  **Input**: Protein sequences in FASTA format
-  **Sources**: UniProt
-  **Size**: 8000 ezymes / 8000 not enzymes
-  **Split**: 80% training, 20% testing (stratified)

## Models:
**Random Forest**
-    Baseline model using ESM-C embeddings
-   Used GridSearchCV for best parameters

**Multi-Layer Perceptron (MLP)**
-   Input: ESM-C embeddings (960 dimensions)
-   Architecture: 3 hidden layers: 1024/512/256 neurons
-   Loss: Binary Cross-Entropy with Logits Loss
-   Optimizer: Adam, lr = 0.0012

## Results:
**Random forest**: 
-   Accuracy: 0.777 
-   F1-score: 0.778
   
**MLP**:
-  Accuracy: 0.949
-  F1-score: 0.945

## Usage:
  **Training Models**:
    Run the Jupyter notebook to train both models:
  ```bash
      jupyter notebook learning_models.ipynb
  ```
    
  **Making Predictions**:
    Launch the GUI application:   
  ```bash
      python predict_enzyme.py
  ```

## Requirements:
  See requirements.txt for complete list of dependencies

## References:
    @software{evolutionaryscale_2024,
    author = {{EvolutionaryScale Team}},
    title = {evolutionaryscale/esm},
    year = {2024},
    publisher = {Zenodo},
    doi = {10.5281/zenodo.14219303},
    URL = {https://doi.org/10.5281/zenodo.14219303}
