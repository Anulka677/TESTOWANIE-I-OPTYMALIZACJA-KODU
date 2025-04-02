import cv2
import numpy as np

image = cv2.imread("mops.jpg")

M = np.ones(image.shape, dtype="uint8") * 150

numpy_burned = image + M

opencv_burned = cv2.add(image, M)

cv2.imshow("NumPy", numpy_burned)
cv2.imshow("OpenCV", opencv_burned)
cv2.waitKey(0)
cv2.destroyAllWindows()
