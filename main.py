from flask import Flask, request
from flask_cors import CORS, cross_origin  # Import CORS
import pandas as pd
import numpy as np
from flask import jsonify
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

pickle_in = open("hr_analytics.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "hello welcome"



@app.route('/predict')
def prediction_authentication():
    try:
        experience = float(request.args.get("experience"))
        test_score = float(request.args.get("test_score"))
        interview_score = float(request.args.get("interview_score"))
        prediction = classifier.predict([[experience, test_score, interview_score]])
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

