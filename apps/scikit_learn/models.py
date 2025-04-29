from django.db import models

# Create your models here.
from sklearn.linear_model import LogisticRegression
import numpy as np
import joblib

# Train a basic model
X = np.array([[0], [1], [2], [3]])
y = np.array([0, 0, 1, 1])

model = LogisticRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
