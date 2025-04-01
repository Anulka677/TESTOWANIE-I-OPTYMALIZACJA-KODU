import cv2

image = cv2.imread('zwierz.jpg')

width = image.shape[1]

right_half = image[:, width//2 :]

cv2.imshow('tylko prawa połowa', right_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
