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

mean_image = cv2.blur(noisy_image, (5, 5))

gaussian_image = cv2.GaussianBlur(noisy_image, (5, 5), 0)

median_image = cv2.medianBlur(noisy_image, 5)

cv2.imwrite("output_mean.png", mean_image)
cv2.imwrite("output_gaussian.png", gaussian_image)
cv2.imwrite("output_median.png", median_image)

print("Salt-and-pepper noise added.")
print("Mean filter applied.")
print("Gaussian filter applied.")
print("Median filter applied.")
print("All filtered images saved successfully.")
