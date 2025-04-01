import cv2

image = cv2.imread("syd.jpg")

height, width = image.shape[:2]

tile_h = height // 3
tile_w = width // 3

for i in range(3):
    for j in range(3):
        startY = i * tile_h
        endY = startY + tile_h
        startX = j * tile_w
        endX = startX + tile_w
        tile = image[startY:endY, startX:endX]
        window_name = f"{i}{j}"
        cv2.imshow(window_name, tile)

cv2.waitKey(0)
cv2.destroyAllWindows()
