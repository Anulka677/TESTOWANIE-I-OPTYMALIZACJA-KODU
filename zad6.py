import cv2

image = cv2.imread('dok.jpg', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

binary = cv2.bitwise_not(binary)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

result = cv2.bitwise_not(cleaned)

cv2.imshow("oryginalny", image)
cv2.imshow("oczyszczenie", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
