import cv2

image = cv2.imread('piesek.jpg')

(h, w) = image.shape[:2]

cX, cY = w // 2, h // 2

half_size = 50

image[cY - half_size:cY + half_size, cX - half_size:cX + half_size] = (0, 0, 255)

cv2.imshow("zmieniony", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
