import cv2
import numpy as np

image = cv2.imread("syd1.jpeg")

mask = np.ones(image.shape, dtype="uint8") * 255

start_point = (image.shape[1] // 2 - 50, image.shape[0] // 2 - 30 - 20)
end_point   = (image.shape[1] // 2 + 10, image.shape[0] // 2 - 15 - 20)

cv2.rectangle(mask, start_point, end_point, (0, 0, 0), -1)

hidden = cv2.bitwise_and(image, mask)

cv2.imshow("zasłonięte oczy", hidden)
cv2.waitKey(0)
cv2.destroyAllWindows()
