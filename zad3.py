import cv2
import numpy as np

image = cv2.imread("slonie.jpg")

(B, G, R) = cv2.split(image)

swapped = cv2.merge([R, B, G])
cv2.imshow("R, B, G", swapped)

G_zero = np.zeros_like(G)
no_green = cv2.merge([B, G_zero, R])
cv2.imshow("no green channel", no_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
