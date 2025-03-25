import cv2
import imutils

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

resized = imutils.resize(image, width=500)

cv2.imshow("szerokość 500 px", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
