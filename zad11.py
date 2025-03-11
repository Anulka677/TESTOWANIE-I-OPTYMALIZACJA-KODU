import cv2

image = cv2.imread('piesek.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

print(f"Współrzędne: {maxLoc}, wartość: {maxVal}")
