import cv2

image = cv2.imread("piesek.jpg")
cv2.imshow("oryginalny", image)

blur = cv2.blur(image, (15, 15))
cv2.imshow("proste rozmycie", blur)

# zalety:
# - proste i szybkie
# - skutecznie usuwa drobny szum
# wady:
# - rozmywa też krawędzie
# - nie zachowuje dobrze szczegółów

gaussian = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("rozmycie Gaussa", gaussian)

# zalety:
# - mniej sztuczne efekty
# wady:
# - może rozmywać krawędzie


median = cv2.medianBlur(image, 15)
cv2.imshow("rozmycie medianowe", median)

# zalety:
# - skuteczne w usuwaniu szumu
# - zachowuje krawędzie lepiej niż blur i gauss
# wady:
# - wolniejsze niż blur

bilateral = cv2.bilateralFilter(image, 11, 61, 39)
cv2.imshow("rozmycie dwustronne", bilateral)

# zalety:
# - usuwa szum i zachowuje ostre krawędzie
# wady:
# - najwolniejsze ze wszystkich
# - wymaga dobrania parametrów

cv2.waitKey(0)
cv2.destroyAllWindows()

#i. Która metoda najlepiej usuwa szum?
#- rozmycie dwustronne

#ii. Która metoda zachowuje najwięcej szczegółów?
#- rozmycie dwustronne

#iii. Jakie są zalety i wady każdej metody? – wypisane w komentarzach wyzej