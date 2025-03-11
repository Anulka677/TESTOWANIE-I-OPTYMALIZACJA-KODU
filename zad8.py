import cv2

image = cv2.imread('piesek.jpg')

cv2.imshow("oryginalny", image)

image[100, :] = (0, 255, 0)

cv2.imshow("zmieniony", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
