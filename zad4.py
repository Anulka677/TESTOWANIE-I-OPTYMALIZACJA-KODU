import numpy as np
import cv2
import imutils

image = cv2.imread("piesek.jpg")

shifted_imutils = imutils.translate(image, 100, 50)

cv2.imshow("przesuniety obraz", shifted_imutils)


cv2.waitKey(0)
cv2.destroyAllWindows()
