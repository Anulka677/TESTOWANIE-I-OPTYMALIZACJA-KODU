import cv2
import imutils

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

resized = imutils.resize(image, height=400)

cv2.imshow("wysokość 400 px", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
