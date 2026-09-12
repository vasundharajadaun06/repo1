import cv2


image = cv2.imread("input.jpg")


if image is None:
    print("Error: input.jpg not found")
    exit()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


height, width = gray.shape

print("Original image shape:", image.shape)
print("Grayscale image shape:", gray.shape)
print("Height:", height)
print("Width:", width)


cv2.imwrite("output.png", gray)

print("Grayscale image saved as output.png")
