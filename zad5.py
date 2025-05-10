import cv2
import numpy as np

image = cv2.imread("kraj.jpg")
cv2.imshow("original", image)

noisy = image.copy()
gaussian_noise = np.zeros_like(image, dtype=np.int16)
cv2.randn(gaussian_noise, (0, 0, 0), (20, 20, 20))
noisy = cv2.add(image.astype(np.int16), gaussian_noise)
noisy = np.clip(noisy, 0, 255).astype(np.uint8)
cv2.imshow("Noisy (Gaussian)", noisy)

blurred_avg = cv2.blur(noisy, (5, 5))
cv2.imshow("Average Blur", blurred_avg)

blurred_gauss = cv2.GaussianBlur(noisy, (5, 5), 0)
cv2.imshow("Gaussian Blur", blurred_gauss)

blurred_median = cv2.medianBlur(noisy, 5)
cv2.imshow("Median Blur", blurred_median)

blurred_bilateral = cv2.bilateralFilter(noisy, 9, 75, 75)
cv2.imshow("Bilateral Blur", blurred_bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

#oceń, która najlepiej usuwa szum, zachowując detale obrazu
#-Bilateral Blur
