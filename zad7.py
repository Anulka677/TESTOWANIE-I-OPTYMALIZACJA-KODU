import cv2
import imutils

image = cv2.imread("kot.jpg")

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_warp = cv2.warpAffine(image, M, (w, h))


rotated_imutils = imutils.rotate(image, 60)


cv2.imshow("warpAffine", rotated_warp)
cv2.imshow("imutils.rotate", rotated_imutils)
cv2.waitKey(0)
cv2.destroyAllWindows()
