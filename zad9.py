import cv2

image = cv2.imread("syd.jpg")

cropped = image[0:300, 0:300]

cv2.imwrite("cropped_image.jpg", cropped)
