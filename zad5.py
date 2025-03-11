import cv2

image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

half_h, half_w = h // 2, w // 2

image[0:half_h, 0:half_w] = (255, 0, 0)

cv2.imshow("zmieniony", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
