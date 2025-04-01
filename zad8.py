import cv2

image = cv2.imread("syd.jpg")

roi_width = 400
step = 10
x = 0

max_width = image.shape[1]


while True:
    if x + roi_width > max_width:
        break

    roi = image[:, x:x + roi_width]

    cv2.imshow("przesuwanie kamery", roi)

    key = cv2.waitKey(0)

    x += step

cv2.destroyAllWindows()
