import cv2

image = cv2.imread("syd.jpg")

fragment = image[50:150, 200:300]

image[0:100, 0:100] = fragment

cv2.imshow("kopiowanie i wklejanie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
