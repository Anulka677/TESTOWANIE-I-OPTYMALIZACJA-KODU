import cv2


image = cv2.imread('zad4.jpg', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

binary = cv2.bitwise_not(binary)

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))



closed_rect = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_rect)
closed_ellipse = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_ellipse)


cv2.imshow("oryginalny", binary)
cv2.imshow("prostokatny", closed_rect)
cv2.imshow("eliptyczny", closed_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()
