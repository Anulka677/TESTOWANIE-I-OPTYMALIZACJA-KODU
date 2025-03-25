import cv2

image = cv2.imread("devon.jpg")
cv2.imshow("oryginalny", image)

flipped = cv2.flip(image, 0)

cv2.imshow("odbicie pionowe", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
