from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

def evaluation_metrics(y_test, y_predict):

    # Calculate evaluation metrics
    accuracy = accuracy_score(y_test, y_predict)
    f1 = f1_score(y_test, y_predict, average='weighted')
    conf_matrix = confusion_matrix(y_test, y_predict)

    return accuracy, f1, conf_matrix