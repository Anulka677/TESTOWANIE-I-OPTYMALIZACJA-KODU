import cv2

image = cv2.imread('syd.jpg')

roi = image[270:380, 200:350]

cv2.imshow('sydney', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
