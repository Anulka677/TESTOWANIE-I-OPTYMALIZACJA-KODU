import cv2

image1 = cv2.imread("IMG_3670.PNG")
image2 = cv2.imread("IMG_3671.PNG")

if image1.shape != image2.shape:
    print("różne rozmiary")
else:
    diff = cv2.absdiff(image1, image2)

    cv2.imshow("moj kotek 1", image1)
    cv2.imshow("moj kotek 2", image2)
    cv2.imshow("roznice", diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
