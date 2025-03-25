import cv2

image = cv2.imread("devon.jpg")

(h, w) = image.shape[:2]

right_half = image[0:h, w//2:w]

flipped_half = cv2.flip(right_half, 1)

image[0:h, w//2:w] = flipped_half

cv2.imshow("wynik", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
