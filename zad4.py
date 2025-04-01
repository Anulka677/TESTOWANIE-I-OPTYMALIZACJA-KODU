import cv2

image = cv2.imread('zwierz.jpg')

startX = int(input("start X: "))
endX = int(input("end X: "))
startY = int(input("start Y: "))
endY = int(input("end Y: "))

roi = image[startY:endY, startX:endX]

cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
