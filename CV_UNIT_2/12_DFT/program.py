import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

image_float = np.float32(image)

dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

magnitude = np.log1p(magnitude)

magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

magnitude = np.uint8(magnitude)

print("Original image shape:", image.shape)
print("DFT shape:", dft.shape)
print("Shifted DFT shape:", dft_shift.shape)

cv2.imwrite("output.png", magnitude)

print("DFT output saved as output.png")
