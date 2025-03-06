import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Simulated example data (Replace this with your actual frame confidence scores)
frames = np.arange(1, 110)  # 109 frames
confidence_scores = np.random.uniform(0.4, 0.55, len(frames))  # Sample confidence values

# Apply Gaussian smoothing for trend line (Change sigma for more/less smoothness)
smoothed_scores = gaussian_filter1d(confidence_scores, sigma=3)

# Create figure and axis
plt.figure(figsize=(12, 6))

# Plot actual confidence scores
plt.plot(frames, confidence_scores, 'bo-', markersize=4, alpha=0.6, label="Confidence Score")

# Plot smoothed trend line
plt.plot(frames, smoothed_scores, color='darkorange', linewidth=2.5, label="Smoothed Trend")

# Add threshold line
threshold = 0.5
plt.axhline(y=threshold, color='red', linestyle='dashed', linewidth=2, label="Threshold (0.5)")
plt.text(frames[-1] + 2, threshold, "Threshold (0.5)", color='red', fontsize=12, verticalalignment='bottom')

# Adjust x-axis for better readability
plt.xticks(np.arange(0, len(frames) + 1, step=10))  # Show every 10th frame
plt.xlabel("Frame", fontsize=12)
plt.ylabel("Confidence (0-1)", fontsize=12)
plt.title("Deepfake Detection Confidence Graph", fontsize=14, fontweight='bold')

# Add grid for better visual separation
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)

# Customize legend placement
plt.legend(loc="upper right", fontsize=11)

# Show final optimized graph
plt.tight_layout()
plt.show()
