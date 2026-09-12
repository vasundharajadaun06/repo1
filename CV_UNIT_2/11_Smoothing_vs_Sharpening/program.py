import cv2
import numpy as np

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

smooth_image = cv2.GaussianBlur(image, (5, 5), 0)

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp_image = cv2.filter2D(image, -1, kernel)

cv2.imwrite("output_smooth.png", smooth_image)
cv2.imwrite("output_sharp.png", sharp_image)

print("Smoothing applied using Gaussian filter.")
print("Sharpening applied using custom kernel.")
print("Smooth image saved as output_smooth.png")
print("Sharp image saved as output_sharp.png")
