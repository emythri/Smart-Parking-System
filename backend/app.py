from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Allow importing from model folder
sys.path.append(os.path.abspath(".."))

from part2 import predict  # your prediction function

app = Flask(__name__)
CORS(app)

# Prediction route
@app.route("/predict", methods=["POST"])
def make_prediction():
    try:
        data = request.json  # input from frontend
        input_data = data["input"]  # expecting {"input": [...]}

        result = predict(input_data)

        return jsonify({
            "prediction": str(result)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import sys
# import os

# # Allow importing from model folder
# sys.path.append(os.path.abspath(".."))

# from part2 import predict  # your prediction function

# app = Flask(__name__)
# CORS(app)

# # Home route
# @app.route("/")
# def home():
#     return "API is running"

# # Prediction route
# @app.route("/predict", methods=["POST"])
# def make_prediction():
#     try:
#         data = request.json  # input from frontend
#         input_data = data["input"]  # expecting {"input": [...]}

#         result = predict(input_data)

#         return jsonify({
#             "prediction": str(result)
#         })

#     except Exception as e:
#         return jsonify({
#             "error": str(e)
#         })

# if __name__ == "__main__":
#     app.run(debug=True)