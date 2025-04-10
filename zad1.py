import cv2
import numpy as np

image = cv2.imread("syd1.jpeg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.ellipse(mask, (image.shape[1] // 2, image.shape[0] // 2), (100, 130), 0, 0, 360, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("po maskowaniu twarzy", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
