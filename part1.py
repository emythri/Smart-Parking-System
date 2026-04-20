# part1.py

import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# Example training data (replace with your dataset)
# X = features, y = labels
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [5, 6, 7]
])

y = np.array([0, 0, 1, 1])

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")