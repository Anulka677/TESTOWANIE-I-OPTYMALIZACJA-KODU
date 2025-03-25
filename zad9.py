import cv2

image = cv2.imread("obraz.jpg")
cv2.imshow("oryginalny", image)
cv2.waitKey(500)

scales = [1.0 + i * 0.2 for i in range(11)]  #[1.0,1.2,1.4,...,3.0]

for scale in scales:
    new_width = int(image.shape[1] * scale)
    new_height = int(image.shape[0] * scale)
    dim = (new_width, new_height)

    resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(f"skal {int(scale * 100)}%", resized)
    cv2.waitKey(500)

cv2.destroyAllWindows()
