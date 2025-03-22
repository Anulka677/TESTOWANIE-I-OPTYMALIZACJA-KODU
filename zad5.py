import cv2
import imutils

image = cv2.imread("kot.jpg")

rotated = imutils.rotate(image, 180)

cv2.imshow("wynik", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
