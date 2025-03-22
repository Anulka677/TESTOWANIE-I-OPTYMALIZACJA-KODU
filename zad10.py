import cv2

image = cv2.imread("kot.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

for angle in range(0, 361, 15):
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))

    cv2.imshow("wynik", rotated)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
