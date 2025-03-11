import cv2

image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

x, y = map(int, input("Podaj współrzędne piksela (x y): ").split())

if 0 <= x < w and 0 <= y < h:
    image[y, x] = (0, 0, 0)

    cv2.imshow("zmieniony", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Podane współrzędne są poza zakresem obrazu")