import cv2

image = cv2.imread('piesek.jpg')

(b1, g1, r1) = image[40, 60]
(b2, g2, r2) = image[250, 100]

diff_r = abs(r1 - r2)
diff_g = abs(g1 - g2)
diff_b = abs(b1 - b2)

print(f"Pixel at (40,60) - Red: {r1}, Green: {g1}, Blue: {b1}")
print(f"Pixel at (250,100) - Red: {r2}, Green: {g2}, Blue: {b2}")
print(f"R: {diff_r}, G: {diff_g}, B: {diff_b}")
