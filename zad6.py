import cv2

image = cv2.imread("devon.jpg")

cv2.imshow("oryginalny", image)

flip_code = int(input("sposób odbicia: 0 - pionowe, 1 - poziome, -1 - oba: "))

flipped = cv2.flip(image, flip_code)
cv2.imshow("po odbiciu", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
