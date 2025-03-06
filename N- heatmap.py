import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2

# Load inference results from JSON file
json_path = "inference_results.json"
with open(json_path, "r") as f:
    results = json.load(f)

# Extract frame names and confidence scores
frames = []
confidences = []

for entry in results:
    frames.append(entry["frame"])
    confidences.append(entry["confidence"])

# Convert to numpy array
confidences = np.array(confidences).reshape(-1, 1)  # Reshape for heatmap compatibility

# Generate heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(confidences.T, cmap="coolwarm", annot=True, fmt=".2f", cbar=True, xticklabels=frames, yticklabels=["Confidence"])
plt.xlabel("Frame Number")
plt.ylabel("Confidence Score")
plt.title("Deepfake Detection Heatmap")
plt.xticks(rotation=90)
plt.tight_layout()

# Save and display the heatmap
heatmap_path = "confidence_heatmap.png"
plt.savefig(heatmap_path, dpi=300)
plt.show()

print(f"✅ Heatmap saved as {heatmap_path}")
