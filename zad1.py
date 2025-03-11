import cv2

image = cv2.imread('piesek.jpg')

(b, g, r) = image[0, 0]
print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")
