import cv2
import os

# Video path
video_path = "input_video.mp4"  # Change this to your actual video file

# Check if the file exists before opening
if not os.path.exists(video_path):
    print(f"❌ Error: Video file '{video_path}' not found. Place it in the project directory.")
else:
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Error: Could not open video file. Check the format or path!")
    else:
        print(f"✅ Video '{video_path}' loaded successfully!")

    cap.release()
