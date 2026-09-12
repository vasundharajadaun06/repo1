import cv2
import numpy as np

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened_image = cv2.filter2D(image, -1, kernel)

cv2.imwrite("output.png", sharpened_image)

print("Sharpening kernel:")
print(kernel)
print("Sharpened image saved as output.png")
