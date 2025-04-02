import cv2
import numpy as np

image = cv2.imread("mops.jpg")

(B, G, R) = cv2.split(image)

add_10 = np.full(B.shape, 10, dtype="uint8")
sub_20 = np.full(G.shape, 20, dtype="uint8")
add_30 = np.full(R.shape, 30, dtype="uint8")

B = cv2.add(B, add_10)      # niebieski +10
G = cv2.subtract(G, sub_20) # zielony -20
R = cv2.add(R, add_30)      # czerwony +30

filtered = cv2.merge([B, G, R])

cv2.imshow("instagram filtr", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
