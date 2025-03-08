# Deepfake-Detection-
# Deepfake Detection MVP

## Overview

This repository contains the **Deepfake Detection MVP**, a lightweight model designed to detect deepfake videos/images using advanced AI techniques. The project consists of a **frontend (UI)** for user interaction and a **backend (API + model inference engine)** for deepfake analysis.

---

## Code Structure

```
Deepfake-Detection-Project
│
├── 📁 backend
│   ├── N-heatmap.py
│   ├── N-analyse vid.py
│   ├── N-confidence graph.py
│   ├── N-load model.py
│   ├── N-run inference and save.py
│
├── 📁 frontend
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│
├── 📁 .vscode
│   ├── launch.json
│
├── 📁 models
│   ├── xception_model.h5
│
├── 📁 dataset
│   ├── real_videos/
│   ├── deepfake_videos/
│
├── README.md
├── requirements.txt

---

## Dependencies

### Frontend:

- HTML, CSS, JavaScript
- Fetch API for HTTP requests

### Backend:

- Python 3.8+
- Flask
- OpenCV
- NumPy
- ONNX Runtime (for optimized inference)
- TensorFlow/PyTorch (if using a different model)

Install dependencies using:

```bash
pip install -r backend/requirements.txt
```

---

## Setup & Execution

### 1️⃣ Backend Setup:

```bash
git clone https://github.com/yourrepo/deepfake-detection-mvp.git
cd deepfake-detection-mvp/backend
python main.py
```

The Flask server will start at [**http://127.0.0.1:5000**](http://127.0.0.1:5000)

### 2️⃣ Frontend Setup:

Simply open `frontend/index.html` in a browser OR serve it using a local server:

```bash
cd frontend
python -m http.server 8000
```

Access the frontend at [**http://127.0.0.1:8000**](http://127.0.0.1:8000)

---

## API Endpoints

- `` – Uploads an image/video and returns detection results.
  ```json
  {
    "image": "base64-encoded-image",
    "video": "base64-encoded-video"
  }
  ```
- **Response:**
  ```json
  {
    "prediction": "Deepfake | Real",
    "confidence": 0.98,
    "heatmap": "base64-encoded-heatmap"
  }
  ```

---

## Expected Output

- If a deepfake is detected, the UI will display a **warning message**.
- A **heatmap** (if enabled) will highlight manipulated regions.
- Model confidence score is shown.

---

## Additional Considerations

- The MVP is **lightweight**, focusing on **speed & efficiency**.
- Model optimization via **ONNX & TensorRT** is planned for future releases.
- Further **real-time inference** improvements may include frame selection & temporal consistency analysis.

For contributions or issues, feel free to open a GitHub issue!

---

### 🚀 Future Enhancements

- Support for **live video deepfake detection**.
- **Mobile & browser extensions** for real-time scanning.
- More **robust adversarial training** to prevent dataset overfitting.

---

*Developed by Shriram & Team* 🎯

