import cv2

image = cv2.imread("tekst.png")
cv2.imshow("oryginalny", image)

for k in [3, 9, 15]:
    blur = cv2.blur(image, (k, k))
    cv2.imshow(f"Średnie blur {k}x{k}", blur)

for k in [3, 9, 15]:
    gauss = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"Gauss {k}x{k}", gauss)

for k in [3, 9, 15]:
    median = cv2.medianBlur(image, k)
    cv2.imshow(f"Medianowe {k}", median)

params = [
    (9, 75, 75),
    (11, 100, 100),
    (15, 150, 150)
]
for (d, sigmaColor, sigmaSpace) in params:
    bilateral = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    cv2.imshow(f"Bilateral d={d}, sc={sigmaColor}, ss={sigmaSpace}", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

#i. Które metody najmocniej rozmywają tekst?
# medianowe, gauss i srednie blur przy dużych kernalach najbardziej

#ii. Które pozwalają zachować jego czytelność?
# rozmycie dwustronne najlepiej zachowuje czytelnosc
