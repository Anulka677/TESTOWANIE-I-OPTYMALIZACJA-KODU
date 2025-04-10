import cv2
import numpy as np

logo = cv2.imread("logo.jpg")

(B, G, R) = cv2.split(logo)

swapped = cv2.merge([R, G, B])


zero_channel = np.zeros_like(G)
no_green = cv2.merge([B, zero_channel, R])

cv2.imshow("oryginalne logo", logo)
cv2.imshow("zamienione kanały", swapped)
cv2.imshow("bez kanału zielonego", no_green)
cv2.waitKey(0)
cv2.destroyAllWindows()
