import cv2

image = cv2.imread("widok.jpg")
cv2.imshow("oryginalny", image)

params = [
    (9, 75, 75),
    (11, 100, 100),
    (15, 150, 150)
]

for (diameter, sigmaColor, sigmaSpace) in params:
    bilateral = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = f"Bilateral d={diameter}, sc={sigmaColor}, ss={sigmaSpace}"
    cv2.imshow(title, bilateral)


blur = cv2.blur(image, (9, 9))
cv2.imshow("Proste rozmycie", blur)

gaussian = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow("Rozmycie Gaussa", gaussian)

median = cv2.medianBlur(image, 9)
cv2.imshow("Rozmycie medianowe", median)

cv2.waitKey(0)
cv2.destroyAllWindows()

#i. Czy rozmycie dwustronne skutecznie redukuje szum?
#tak zwłaszcza przy większych wartościach sc i ss - szum znika ale krawędzie są zachowane

#ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
#tak, krawedzie tez sa ok w rozmyciu medianowym

#iii. Jakie wartości parametrów dają najlepsze rezultaty?
#d=9–11, sc=75–100, ss=75–100
#zbyt wysokie wartości mogą spowodować nienaturalny efekt
