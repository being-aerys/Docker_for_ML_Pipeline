# Created by Aashish Adhikari at 9:50 AM 7/17/2021

from flask import Flask, request, jsonify
from flasgger import Swagger # a Flask extention to create flask API's using documentation --> provides API specs in the docstrings.

import pickle
import numpy as np
import pandas as pd

'''load the learned svm model'''
with open("svm_model.pkl", "rb") as svm_model_pkl:
    svm_model = pickle.load(svm_model_pkl)


'''Create a flask app'''
ml_app = Flask(__name__)
swagger = Swagger(ml_app)

@ml_app.route("/predict", methods = ["GET"])
def predict_svm_sample():
    """Endpoint to predict the class of a specific sample using the loaded SVM. [0: Setosa, 1: Versicolor, 2: Virginica]
    ---
    parameters:
        - name: sepal_length
          in: query
          type: number
          required: True
        - name: sepal_width
          in: query
          type: number
          required: True
        - name: petal_length
          in: query
          type: number
          required: True
        - name: petal_width
          in: query
          type: number
          required: True
    responses:
      200:
        description: Index of predicted class
    """
    sepal_length = request.args.get("sepal_length")
    sepal_width = request.args.get("sepal_width")
    petal_length = request.args.get("petal_length")
    petal_width = request.args.get("petal_width")
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = svm_model.predict(features)
    return str(prediction)

    # prediction_dict = dict{}
    # prediction_dict["solution"] = prediction
    #return str(prediction_dict)
    #return jsonify({"prediction": prediction})

@ml_app.route("/predict_a_batch", methods = ["POST"])
def predict_a_batch():
    """Endpoint to predict the classes of a batch of samples using the loaded SVM.
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: True
    """
    samples = pd.read_csv(request.files.get("input_file"), header = None)
    predictions = svm_model.predict(samples)
    return str(list(predictions))

if __name__ == "__main__":
    ml_app.run(host="0.0.0.0", port=8888)