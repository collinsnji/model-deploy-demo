import joblib
from sklearn.datasets import make_classification

def make_prediction(prediction_data):
    """Load the model from disk, and make a prediction.
    
    Args:
        prediction_data (np.ndarray): The data to make a prediction on.
    Returns:
        int: The predicted class as an integer.
    """
    model = joblib.load('models/model.pkl')
    y_pred = model.predict(prediction_data)
    return y_pred[0]

if __name__ == '__main__':
    data, _ = make_classification(n_samples=1, n_features=4, random_state=42)
    y_pred = make_prediction(data)
    print(y_pred)
