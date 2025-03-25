import cv2

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)

width = int(image.shape[1] * 0.2)
height = int(image.shape[0] * 0.2)
dim = (width, height)

methods = [
    ("INTER_AREA", cv2.INTER_AREA),
    ("INTER_NEAREST", cv2.INTER_NEAREST),
    ("INTER_LINEAR", cv2.INTER_LINEAR),
    ("INTER_CUBIC", cv2.INTER_CUBIC),
    ("INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

for (name, method) in methods:
    resized = cv2.resize(image, dim, interpolation=method)
    cv2.imshow(f"m - {name}", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
