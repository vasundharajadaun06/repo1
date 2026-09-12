import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()
  
min_value = np.min(image)
max_value = np.max(image)

print("Minimum intensity:", min_value)
print("Maximum intensity:", max_value)

if max_value == min_value:
    stretched = image.copy()
else:
    stretched = (image - min_value) * 255.0 / (max_value - min_value)

stretched = np.clip(stretched, 0, 255)

stretched = stretched.astype(np.uint8)

cv2.imwrite("output.png", stretched)

print("Contrast stretched image saved as output.png")
