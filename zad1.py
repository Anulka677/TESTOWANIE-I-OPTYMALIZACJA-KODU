import numpy as np
import cv2

canvas_size = 300

circle = np.zeros((canvas_size, canvas_size), dtype="uint8")
cv2.circle(circle, (150, 150), 100, 255, -1)
cv2.imshow("circle", circle)

triangle = np.zeros((canvas_size, canvas_size), dtype="uint8")
points = np.array([[150, 50], [50, 250], [250, 250]])
cv2.drawContours(triangle, [points], 0, 255, -1)
cv2.imshow("triangle", triangle)

bitwiseAnd = cv2.bitwise_and(triangle, circle)
cv2.imshow("AND", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(triangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(triangle, circle)
cv2.imshow("XOR", bitwiseXor)

bitwiseNot = cv2.bitwise_not(triangle)
cv2.imshow("NOT (triangle)", bitwiseNot)

cv2.waitKey(0)
cv2.destroyAllWindows()
