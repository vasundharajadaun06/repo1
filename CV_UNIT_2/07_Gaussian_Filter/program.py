import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite("output.png", gaussian_image)

print("Gaussian filter applied using 5x5 kernel.")
print("Gaussian filtered image saved as output.png")
