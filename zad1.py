import numpy as np
import cv2

image = cv2.imread("piesek.jpg")
cv2.imshow("oryginalne", image)

M = np.float32([[1, 0, 30], [0, 1, 40]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("wynik", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
