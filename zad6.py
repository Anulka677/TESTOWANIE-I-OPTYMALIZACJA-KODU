import cv2
import numpy as np

image = cv2.imread("pies-w-polu-pszenicy.jpg")

mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.rectangle(mask, (250, 20), (600, 410), 255, -1)

mask_inv = cv2.bitwise_not(mask)

blurred = cv2.GaussianBlur(image, (21, 21), 0)

background = cv2.bitwise_and(blurred, blurred, mask=mask_inv)

foreground = cv2.bitwise_and(image, image, mask=mask)

result = cv2.add(foreground, background)

cv2.imshow("original", image)
cv2.imshow("Depth of Field Simulation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
