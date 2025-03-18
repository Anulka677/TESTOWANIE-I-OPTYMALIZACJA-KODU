import cv2
import numpy as np

image = cv2.imread("zad6.jpg")
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv2.circle(image, (500, 360), 30, red, -1)
cv2.circle(image, (680, 360), 30, red, -1)
cv2.rectangle(image, (520, 520), (660, 560), green, -1)
cv2.circle(image, (570, 410), 250, blue, 2)

cv2.imshow("profilowe zdjęcie osoby", image)
cv2.waitKey(0)
cv2.destroyAllWindows()