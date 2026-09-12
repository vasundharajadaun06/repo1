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

magnitude_spectrum = np.log1p(magnitude)

magnitude_spectrum = cv2.normalize(
    magnitude_spectrum,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

magnitude_spectrum = np.uint8(magnitude_spectrum)

cv2.imwrite("output.png", magnitude_spectrum)

print("Magnitude spectrum generated successfully.")
print("Magnitude spectrum saved as output.png")
