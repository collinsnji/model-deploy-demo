# Deploying a Machine Learning Model to Production
### Author: [Collins Nji](https://collingrimm.com)
### Date: September 14th, 2022

_This repository was prepared for a Small Talk at Mount St. Mary's University on September 14th, 2022._
_It is for demonstration purposes only, and is not intended for full production use without further modification._

## Overview
In this repository, we will be deploying a machine learning model to production using Google Cloud Platform. We will go over how to setup experiments in [MLFlow](https://mlflow.org) to track model iterations and then save our model for deployment. We will be using the [Google Cloud SDK](https://cloud.google.com/sdk) to deploy our model to the cloud, and finally, we will also be using [GitHub Actions](https://github.com/features/actions) to automate the deployment process.

## Setup
To get started, you will need to install the following:
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

After installing the tools above, clone the repository by running:
```bash
$ git clone https://github.com/collinsnji/model-deploy-demo.git
```
> Note: I recommend using a Python virtual environment in order to preserve the main Python ENV on your system
> Follow the instructions [here](https://docs.python.org/3/library/venv.html) to setup a Python virtual environment.

Install project dependencies using PIP
```bash
$ pip install -r requirements.txt
```

## Train Model
The model training script builds a very simple model using the [Iris Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) from the Scikit Learn library.

#### Train the model by running:
```bash
$ python src/train.py
```

After the model training step completes, you should see a `model.pkl` file generated, which simply holds the training weights of the generated model.

#### Experiments With MLFlow
You can track experiments with MLFlow by running
```bash
$ cd src
$ mlflow ui
```

## Serving the Model on a REST API
Included in this tutorial is a simple REST API written with Python Flask which allows serving the model. To run the REST API, do the following:

```bash
$ python src/serve.py
```
This will serve the model on http://localhost:4500/.

To test that the API is running, we can send a cURL POST request to the API by running:
```bash
$ curl --request POST \
  --url http://127.0.0.1:8090/predict \
  --header 'Content-Type: application/json' \
  --data '{
	"sepallength(cm)": [5.3],
	"sepalwidth(cm)": [2.5],
	"petallength(cm)": [4.6],
	"petalwidth(cm)": [1.9]
}'
```
You should get a response that looks similar to:
```json
{ "prediction": "virginica" }
```
Which means that our API is up and running, and is able to make/fulfill requests.
