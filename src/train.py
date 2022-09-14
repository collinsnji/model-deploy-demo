import tempfile
from datetime import datetime

import joblib
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
from from_root import from_root
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             plot_confusion_matrix)
from sklearn.model_selection import train_test_split


def display_data():
    """Display the data."""
    iris = load_iris()
    iris.feature_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
    print(iris.feature_names)
    print(iris.target_names)

def split_data():
    """ Load the iris data, and split it into training and testing data."""
    iris_data = load_iris()
    X = iris_data.data
    y = iris_data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_train, X_test, y_train, y_test

def build_model(X_train, y_train) -> RandomForestClassifier:
    """Build a random forest model using the training data, and return the model.

    Args:
        X_train (np.ndarray): Training data features.
        y_train (np.ndarray): Training data labels.

    Returns:
        RandomForestClassifier: A random forest model.
    """
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    return model

def write_model_to_disk(model, folder_path=None):
    """Write the model to disk.
    
    Args:
        model (RandomForestClassifier): A random forest model.
        folder_path (str): The path to write the model to. Defaults to None.
    """
    ROOT_DIR = from_root().absolute()
    if folder_path is None:
        joblib.dump(model, f'{ROOT_DIR}/models/model.pkl')
    else:
        joblib.dump(model, f"{folder_path}/model.pkl")

def model_metrics(model, X_test, y_test):
    """Calculate the model metrics and return the accuracy and confusion matrix.

    Args:
        model (RandomForestClassifier): A random forest model.
        X_test (np.ndarray): Testing data features.
        y_test (np.ndarray): Testing data labels.
    """
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred), confusion_matrix(y_test, y_pred)

def train_model():
    """Run the train_model function which trains the model, writes it to disk as well as track the 
        model metrics in MLflow.
    """
    X_train, X_test, y_train, y_test = split_data()
    
    # Initialize the MLflow tracking server
    with mlflow.start_run():
        model = build_model(X_train=X_train, y_train=y_train)
        write_model_to_disk(model)
        accuracy, _ = model_metrics(model, X_test, y_test)
        # Log the model metrics to MLflow
        with tempfile.TemporaryDirectory() as tempdir:
            plot_confusion_matrix(model, X_test, y_test, display_labels=load_iris().target_names, cmap='Blues',)
            plt.savefig(tempdir + '/confusion_matrix.png')
            mlflow.log_artifact(tempdir + '/confusion_matrix.png', 'confusion_matrix')
        mlflow.log_param('n_estimators', 100)
        mlflow.log_metric('accuracy', accuracy)
        mlflow.sklearn.log_model(model, f'model-{datetime.isoformat(datetime.now())}')
        datetime.isoformat(datetime.now())

if __name__ == "__main__":
    """Run the training function."""
    train_model()
