import cv2

image = cv2.imread("kot.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

angle = float(input("Podaj kąt obrotu: "))

M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("wynik", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()