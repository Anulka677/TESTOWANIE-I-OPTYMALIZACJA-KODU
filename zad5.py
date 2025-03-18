import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
white = (255, 255, 255)
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for size in range(20, 160, 20):
    top_left = (centerX - size, centerY - size)
    bottom_right = (centerX + size, centerY + size)
    cv2.rectangle(canvas, top_left, bottom_right, white)

cv2.imshow("kwadraty", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()