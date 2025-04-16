import cv2

image = cv2.imread('tekst.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

kernel_shapes = {
    "kwadrat": cv2.MORPH_RECT,
    "elipsa": cv2.MORPH_ELLIPSE,
    "krzyx": cv2.MORPH_CROSS
}

kernel_size = (5, 5)

for name, shape in kernel_shapes.items():
    kernel = cv2.getStructuringElement(shape, kernel_size)

    eroded = cv2.erode(binary, kernel)
    dilated = cv2.dilate(binary, kernel)
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow(f"{name} erozja", eroded)
    cv2.imshow(f"{name} dylatacja", dilated)
    cv2.imshow(f"{name} otwarcie", opened)
    cv2.imshow(f"{name} zamknięcie", closed)
    cv2.imshow(f"{name} gradient", gradient)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
