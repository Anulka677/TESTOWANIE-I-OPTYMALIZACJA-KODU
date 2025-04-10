import cv2
import numpy as np

image = cv2.imread("auto.jpg")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

(H, S, V) = cv2.split(hsv)
S = cv2.add(S, 50, mask=mask)
hsv_enhanced = cv2.merge([H, S, V])

result = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)

cv2.imshow("wynik", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
