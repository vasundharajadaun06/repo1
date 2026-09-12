import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

image_float = np.float32(image)

dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

radius = min(rows, cols) // 8

mask = np.zeros((rows, cols, 2), np.float32)

y, x = np.ogrid[:rows, :cols]
distance = (x - ccol) ** 2 + (y - crow) ** 2

mask[distance <= radius ** 2] = 1

filtered_dft = dft_shift * mask

dft_ishift = np.fft.ifftshift(filtered_dft)

filtered_image = cv2.idft(dft_ishift)

filtered_image = cv2.magnitude(
    filtered_image[:, :, 0],
    filtered_image[:, :, 1]
)

filtered_image = cv2.normalize(
    filtered_image,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

filtered_image = np.uint8(filtered_image)

cv2.imwrite("output.png", filtered_image)

print("Frequency low-pass filter applied.")
print("Output saved as output.png")
