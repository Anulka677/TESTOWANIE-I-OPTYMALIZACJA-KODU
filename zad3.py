import cv2
import numpy as np

image = cv2.imread("mops.jpg")

M = np.ones(image.shape, dtype="uint8") * 80

numpy_darker = image - M

opencv_darker = cv2.subtract(image, M)

cv2.imshow("NumPy)", numpy_darker)
cv2.imshow("OpenCV", opencv_darker)
cv2.waitKey(0)
cv2.destroyAllWindows()
