import numpy as np
import cv2
import imutils

image = cv2.imread("piesek.jpg")

tx = int(input("przesunięcie w poziomie: "))
ty = int(input("przesunięcie w pionie: "))

shifted_imutils = imutils.translate(image, tx, ty)


cv2.imshow("przesuniety obraz", shifted_imutils)

cv2.waitKey(0)
cv2.destroyAllWindows()
