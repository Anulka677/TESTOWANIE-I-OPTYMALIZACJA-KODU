import cv2

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

width = image.shape[1] * 4
height = image.shape[0] * 4
dim = (width, height)

resized_cubic = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow("powiekszone 4 razy - INTER_CUBIC", resized_cubic)

resized_lanczos = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("powiekszone 4 razy - INTER_LANCZOS4", resized_lanczos)

cv2.waitKey(0)
cv2.destroyAllWindows()
