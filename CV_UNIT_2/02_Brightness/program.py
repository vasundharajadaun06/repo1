import cv2
import numpy as np

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

brightness_value = 50
y = 100
x = 100

if y >= image.shape[0] or x >= image.shape[1]:
    y = 0
    x = 0

pixel_before = image[y, x].copy()

bright_image = image.astype(np.int16) + brightness_value

# Keep values between 0 and 255
bright_image = np.clip(bright_image, 0, 255)

bright_image = bright_image.astype(np.uint8)

pixel_after = bright_image[y, x]

print("Brightness value added:", brightness_value)
print("Pixel before:", pixel_before)
print("Pixel after:", pixel_after)

cv2.imwrite("output.png", bright_image)

print("Brightened image saved as output.png")
