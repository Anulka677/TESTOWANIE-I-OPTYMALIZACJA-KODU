import cv2


image = cv2.imread('szum.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel_sizes = [(3, 3), (5, 5), (7, 7)]
results = []

for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    results.append((size, opened))


cv2.imshow("oryginalny", binary)
for size, opened in results:
    cv2.imshow(f"otwarcie {size}", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()
