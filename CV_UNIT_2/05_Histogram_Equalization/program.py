import cv2
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

equalized = cv2.equalizeHist(image)

cv2.imwrite("output.png", equalized)

print("Histogram equalized image saved as output.png")

plt.figure(figsize=(10, 5))

plt.hist(image.ravel(), 256, [0, 256], alpha=0.5, label="Original")

plt.hist(equalized.ravel(), 256, [0, 256], alpha=0.5, label="Equalized")

plt.title("Histogram Comparison")
plt.xlabel("Intensity Value")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()

print("Histogram comparison saved as histogram_comparison.png")
