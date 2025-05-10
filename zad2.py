import cv2

image = cv2.imread("bengalski.jpeg")
cv2.imshow("oryginalny", image)

kernel_sizes = [3, 5, 9, 15]

for k in kernel_sizes:
    blurred = cv2.blur(image, (k, k))
    cv2.imshow(f"cv2.blur {k}x{k}", blurred)

for k in kernel_sizes:
    gaussian = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"cv2.GaussianBlur {k}x{k}", gaussian)

for k in kernel_sizes:
    median = cv2.medianBlur(image, k)
    cv2.imshow(f"cv2.medianBlur {k}", median)

#bilateralFilter nie używa kernela w postaci k k tylko średnicy i sigma
for k in kernel_sizes:
    bilateral = cv2.bilateralFilter(image, k, k * 5, k * 5)
    cv2.imshow(f"cv2.bilateralFilter {k}", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

#i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
#im większy kernel tym silniejsze rozmycie
#przy małych wartościach np 3x3 efekt jest subtelny
#przy większych obraz staje się bardzo gładki ale traci dużo szczegółów

#ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
#sla większości przypadków 5x5/9x9
#3x3 redukuje bardzo mało szumu a 15x15 rozmywa zbyt dużo detali
