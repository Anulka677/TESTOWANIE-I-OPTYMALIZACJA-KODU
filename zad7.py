import cv2

image = cv2.imread('piesek.jpg')

(h, w) = image.shape[:2]

part_h, part_w = h // 3, w // 3

center_crop = image[part_h:2*part_h, part_w:2*part_w]

cv2.imshow("frag", center_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
