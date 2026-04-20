import cv2
import numpy as np

def predict(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Simple threshold
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Divide image into grid (example: 3x3 parking)
    h, w = thresh.shape
    rows, cols = 3, 3
    cell_h, cell_w = h // rows, w // cols

    empty = 0
    occupied = 0

    for i in range(rows):
        for j in range(cols):
            cell = thresh[i*cell_h:(i+1)*cell_h, j*cell_w:(j+1)*cell_w]
            white_pixels = np.sum(cell == 255)

            if white_pixels > (cell.size * 0.5):
                empty += 1
            else:
                occupied += 1

    return {
        "empty": empty,
        "occupied": occupied
    }

# # part2.py

# import joblib
# import numpy as np
# import os

# # Load model (make sure correct path)
# model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
# model = joblib.load(model_path)

# def predict(data):
#     try:
#         # Convert input to numpy array
#         data = np.array(data).reshape(1, -1)

#         # Prediction
#         result = model.predict(data)

#         return result.tolist()

#     except Exception as e:
#         return str(e)