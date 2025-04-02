import cv2
import numpy as np

image = cv2.imread("mops.jpg")

M = np.ones(image.shape, dtype="uint8") * 50
numpy_added = image + M

opencv_added = cv2.add(image, M)

cv2.imshow("NumPy", numpy_added)
cv2.imshow("OpenCV", opencv_added)
cv2.waitKey(0)
cv2.destroyAllWindows()
