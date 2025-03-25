import cv2

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

width = int(image.shape[1] * 2)
height = int(image.shape[0] * 2)
dim = (width, height)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

cv2.imshow("powiększony 2 razy", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
