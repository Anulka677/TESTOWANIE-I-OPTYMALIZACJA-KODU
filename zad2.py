import cv2

image = cv2.imread('zwierz.jpg')

height = image.shape[0]

lower_half = image[height//2 : , :]

cv2.imshow('tylko dolna połowa.', lower_half)
cv2.waitKey(0)
cv2.destroyAllWindows()
