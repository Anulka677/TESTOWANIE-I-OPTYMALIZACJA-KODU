import cv2

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

width = int(image.shape[1] * 0.5)
height = int(image.shape[0] * 0.5)
dim = (width, height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("zmniejszony o 50%", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
