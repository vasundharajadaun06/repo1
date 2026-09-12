import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

highest_intensity = np.argmax(histogram)

print("Intensity value with highest frequency:", highest_intensity)

plt.figure(figsize=(10, 5))
plt.plot(histogram)
plt.title("Grayscale Histogram")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.xlim([0, 256])

plt.savefig("output.png", bbox_inches="tight")
plt.close()

print("Histogram saved as output.png")
