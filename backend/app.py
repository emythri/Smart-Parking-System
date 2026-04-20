from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import cv2
import numpy as np
import base64

app = Flask(__name__)
CORS(app)

# Load YOLOv5 model once
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.route("/")
def home():
    return "Parking Detection API Running"

@app.route("/predict", methods=["POST"])
def predict_image():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"})

        file = request.files['file']

        # Convert image to OpenCV format
        img_bytes = file.read()
        npimg = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        if img is None:
            return jsonify({"error": "Invalid image"})

        # Run YOLO detection
        results = model(img)
        detections = results.xyxy[0].cpu().numpy()

        car_count = 0

        # Draw bounding boxes (cars = occupied parking)
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            label = model.names[int(cls)]

            if label == "car":
                car_count += 1
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
                cv2.putText(img, "Occupied", (int(x1), int(y1)-5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        # Convert image to base64
        _, buffer = cv2.imencode('.jpg', img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        print("Cars detected:", car_count)

        return jsonify({
            "image": img_base64,
            "occupied": int(car_count),
            "empty": int(max(0, 10 - car_count))  # assume 10 slots
        })

    except Exception as e:
        return jsonify({"error": str(e)})

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

# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # import sys
# # import os

# # # Allow importing from model folder
# # sys.path.append(os.path.abspath(".."))

# # from part2 import predict  # your prediction function

# # app = Flask(__name__)
# # CORS(app)

# # # Home route
# # @app.route("/")
# # def home():
# #     return "API is running"

# # # Prediction route
# # @app.route("/predict", methods=["POST"])
# # def make_prediction():
# #     try:
# #         data = request.json  # input from frontend
# #         input_data = data["input"]  # expecting {"input": [...]}

# #         result = predict(input_data)

# #         return jsonify({
# #             "prediction": str(result)
# #         })

# #     except Exception as e:
# #         return jsonify({
# #             "error": str(e)
# #         })

# # if __name__ == "__main__":
# #     app.run(debug=True)
