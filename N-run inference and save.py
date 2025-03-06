import numpy as np
import cv2
import onnxruntime as ort
import json  # Import JSON module

# Load the ONNX deepfake detection model
model_path = "xception_deepfake.onnx"
session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])


def preprocess_image(image):
    """Preprocess image for the Xception model (resize & normalize)."""
    image = cv2.resize(image, (299, 299))  # Resize to Xception input size
    image = image.astype(np.float32) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0).transpose(0, 3, 1, 2)  # Channels first for ONNX
    return image


def run_inference(video_path, output_json="predictions.json"):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Error: Could not open video file.")
        return

    frame_count = 0
    predictions = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video

        frame_count += 1
        processed_frame = preprocess_image(frame)  # Preprocess the frame


        # Run inference
        inputs = {session.get_inputs()[0].name: processed_frame}
        output = session.run(None, inputs)[0]

        # Get prediction confidence (between 0 and 1)
        confidence = float(output[0][0])  # Assuming first output node contains probability
        predictions.append({"frame": frame_count, "confidence": confidence})

        print(f"Frame {frame_count}: Deepfake Confidence = {confidence:.4f}")

    cap.release()

    # Save predictions to JSON file
    with open(output_json, "w") as json_file:
        json.dump(predictions, json_file, indent=4)

    print(f"✅ Inference completed successfully! Results saved to {output_json}")
    return predictions


# Run inference on video
video_path = "input_video.mp4"  # Change to your video file
run_inference(video_path)
