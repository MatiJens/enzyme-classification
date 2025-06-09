from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


def random_forest_enzymes(x_train, y_train):
    
    # HIPERPARAMETERS
    N_ESTIMATORS = 100
    MAX_DEPTH = 1
    MIN_SAMPLE_SPLIT = 10
    MIN_SAMPLE_LEAF = 5

    model_random_forest = RandomForestClassifier(
        n_estimators=N_ESTIMATORS,
        max_depth=MAX_DEPTH,
        min_samples_split=MIN_SAMPLE_SPLIT,
        min_samples_leaf=MIN_SAMPLE_LEAF
    )

    model_random_forest.fit(x_train, y_train)

    return model_random_forest

    # Search for best parameters
    model_rf = RandomForestClassifier()

    param_grid = {
        'n_estimators': [100, 200, 500],
        'max_depth': [1, 2, 5, 10],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 5, 10]
    }

    search_param = GridSearchCV(estimator=model_rf,
                                param_grid=param_grid,
                                scoring='accuracy',
                                cv=5,
                                verbose=2)

    search_param.fit(
        x_train,
        y_train
    )

    print(f"Best parameters: {search_param.best_params_}")
    print(f"Best accuracy: {search_param.best_score_}")
    