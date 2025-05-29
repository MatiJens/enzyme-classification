import pandas as pd
from sklearn.model_selection import train_test_split


def split_test_train(enzyme, not_enzyme):

    # Add target value
    enzyme['is_enzyme'] = 1
    not_enzyme['is_enzyme'] = 0

    # Connect enzyme and not enzyme dataframes
    proteins = pd.concat([enzyme, not_enzyme])

    # Split data into features and target / train and test
    x_train, x_test, y_train, y_test = train_test_split(proteins.iloc[:, 0:-2], proteins['is_enzyme'], test_size=0.2, random_state=42, stratify=proteins['is_enzyme'])

    return x_train, x_test, y_train, y_test
