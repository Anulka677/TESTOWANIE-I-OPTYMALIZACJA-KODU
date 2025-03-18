import numpy as np
import cv2

image = cv2.imread("piesek.jpg")
(h, w) = image.shape[:2]

shift_x = w // 2 + 50
shift_y = h // 2 + 50

M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

shifted = cv2.warpAffine(image, M, (w, h))

cv2.imshow("wynik", shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()