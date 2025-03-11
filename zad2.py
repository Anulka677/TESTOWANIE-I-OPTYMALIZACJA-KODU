import cv2

image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]
cv2.imshow("przed", image)
image[h-1, w-1] = (0, 0, 255)

cv2.imshow("po", image)
cv2.waitKey(0)
cv2.destroyAllWindows()