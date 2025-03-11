import cv2

image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
(b, g, r) = image[cY, cX]

print(f"Środek obrazu: ({cX}, {cY})")
print(f"Red: {r}, Green: {g}, Blue: {b}")