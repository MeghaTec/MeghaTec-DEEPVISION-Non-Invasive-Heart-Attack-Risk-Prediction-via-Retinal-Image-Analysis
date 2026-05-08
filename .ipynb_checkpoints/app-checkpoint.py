from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import cv2
import os

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("model/effnet_b0_final.keras")

# Risk mapping
def map_to_heart_risk(dr_class):
    if dr_class == 0:
        return "Low Risk"
    elif dr_class == 1:
        return "Mild Risk"
    elif dr_class == 2:
        return "Moderate Risk"
    elif dr_class == 3:
        return "High Risk"
    else:
        return "Very High Risk"

# Preprocess image
def preprocess_image(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Crop black borders
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    mask = gray > 10
    coords = np.column_stack(np.where(mask))
    if coords.shape[0] > 0:
        y_min, x_min = coords.min(axis=0)
        y_max, x_max = coords.max(axis=0)
        img = img[y_min:y_max, x_min:x_max]

    img = cv2.resize(img, (224,224))

    # CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    r,g,b = cv2.split(img)
    r = clahe.apply(r)
    g = clahe.apply(g)
    b = clahe.apply(b)
    img = cv2.merge((r,g,b))

    img = img.astype(np.float32)

    return np.expand_dims(img, axis=0)

if __name__ == '__main__':
    app.run(debug=True)