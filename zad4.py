import cv2

image = cv2.imread("slonie.jpg")

(B, G, R) = cv2.split(image)

R = cv2.add(R, 50)

enhanced = cv2.merge([B, G, R])

cv2.imshow("wynik", enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
