import cv2
import matplotlib.pyplot as plt

image = cv2.imread('zad2.jpg', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

binary = cv2.bitwise_not(binary)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

white_pixels = []

for i in range(5):
    dilated = cv2.dilate(binary, kernel, iterations=i + 1)
    count_white = cv2.countNonZero(dilated)
    white_pixels.append(count_white)

    cv2.imshow(f"dylatacja {i+1} raz", dilated)
    cv2.waitKey(0)

cv2.destroyAllWindows()

plt.plot(range(1, 6), white_pixels, marker='o')
plt.title('wplyw liczby iteracji dylatacji na grubosc obiektow')
plt.xlabel('ilosc iteracji')
plt.ylabel('ilosc bialych pikseli')
plt.grid(True)
plt.show()
