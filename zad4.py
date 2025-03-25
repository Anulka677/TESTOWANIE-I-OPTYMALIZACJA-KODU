import cv2

image = cv2.imread("devon.jpg")

flipped_horizontal = cv2.flip(image, 1)
flipped_vertical = cv2.flip(image, 0)
flipped_both = cv2.flip(image, -1)

cv2.imshow("oryginalny", image)
cv2.imshow("poziome", flipped_horizontal)
cv2.imshow("pionowe", flipped_vertical)
cv2.imshow("poziome + pionowe", flipped_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
