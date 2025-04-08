import cv2

image1 = cv2.imread("obraz1.png", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("obraz2.png", cv2.IMREAD_GRAYSCALE)


difference = cv2.bitwise_xor(image1, image2)

cv2.imshow("obraz 1", image1)
cv2.imshow("obraz 2", image2)
cv2.imshow("różnice XOR", difference)

cv2.waitKey(0)
cv2.destroyAllWindows()
