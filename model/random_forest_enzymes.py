from sklearn.ensemble import RandomForestClassifier

def random_forest_enzymes(x_train, y_train):

    # HIPERPARAMETERS
    N_ESTIMATORS = 1000
    MAX_DEPTH = 10
    MIN_SAMPLE_SPLIT = 2
    MIN_SAMPLE_LEAF = 1

    model_random_forest = RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        max_depth=MAX_DEPTH,
        min_samples_split=MIN_SAMPLE_SPLIT,
        min_samples_leaf=MIN_SAMPLE_LEAF
    )

    model_random_forest.fit(x_train, y_train)

    return model_random_forest