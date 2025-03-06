import onnxruntime as ort
import numpy as np
import cv2
import os

# Load the optimized ONNX model
model_path = "xception_deepfake.onnx"

# Check if the model file exists before loading
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model file '{model_path}' not found. Place it in the project directory.")

try:
    # Load ONNX model with CPU optimization
    session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")


def preprocess_image(image):
    """Preprocess image for Xception model (resize, convert to RGB, normalize)."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = cv2.resize(image, (299, 299))  # ✅ Correct resizing for Xception
    image = image.astype(np.float32) / 255.0  # ✅ Correct normalization (0-1 scale)
    image = np.transpose(image, (2, 0, 1))  # Convert HWC to CHW (channels first)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image
