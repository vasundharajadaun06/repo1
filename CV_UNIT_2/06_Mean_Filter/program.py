import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

mean_3x3 = cv2.blur(image, (3, 3))

mean_5x5 = cv2.blur(image, (5, 5))

cv2.imwrite("output.png", mean_5x5)

print("3x3 mean filter applied.")
print("5x5 mean filter applied.")
print("Final output saved as output.png")
