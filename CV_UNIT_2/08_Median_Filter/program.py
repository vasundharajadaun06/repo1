import cv2
import numpy as np

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

noisy_image = image.copy()

amount = 0.02
num_pixels = int(amount * image.shape[0] * image.shape[1])

for i in range(num_pixels):
    y = np.random.randint(0, image.shape[0])
    x = np.random.randint(0, image.shape[1])
    noisy_image[y, x] = 255

for i in range(num_pixels):
    y = np.random.randint(0, image.shape[0])
    x = np.random.randint(0, image.shape[1])
    noisy_image[y, x] = 0

median_image = cv2.medianBlur(noisy_image, 5)

cv2.imwrite("output.png", median_image)

print("Salt-and-pepper noise added.")
print("5x5 median filter applied.")
print("Median filtered image saved as output.png")
