import os
import numpy as np
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import io

app = Flask(__name__)

# 1. Load your Kaggle model (Make sure the filename matches)
MODEL_PATH = 'mobilenetv2_garbage_classification.h5'
model = load_model(MODEL_PATH)

# 2. Define classes based on the dataset
CLASSES = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes',
           'green-glass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']

def model_predict(img_bytes):
    # Process the image for the model
    img = Image.open(io.BytesIO(img_bytes))
    img = img.resize((224, 224))  # Match your model's input size
    
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # Normalize if your model expects it
    
    preds = model.predict(x)
    class_idx = np.argmax(preds)
    return CLASSES[class_idx], float(preds[0][class_idx])

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    file = request.files['file']
    img_bytes = file.read()
    
    label, confidence = model_predict(img_bytes)
    
    return jsonify({
        'prediction': label,
        'confidence': f"{confidence*100:.2f}%"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)