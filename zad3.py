import cv2

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

dim = (200, 300)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("200x300", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
