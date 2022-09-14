from flask import Flask, request, jsonify
from app.predict import make_prediction
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return 'Model server is running'

@app.route('/predict', methods=['POST'])
def predict():
    """Load the model from disk, and make a prediction.

    Returns:
        Response: A JSON response with the prediction.
    """
    model_columns = ['sepallength(cm)', 'sepalwidth(cm)', 'petallength(cm)', 'petalwidth(cm)']
    target_names = ['setosa', 'versicolor', 'virginica']
    data_ = request.json
    data = pd.DataFrame(data_)
    query = data.reindex(columns=model_columns, fill_value=0)
    prediction = make_prediction(query)
    return jsonify({'prediction': target_names[prediction]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, debug=True)