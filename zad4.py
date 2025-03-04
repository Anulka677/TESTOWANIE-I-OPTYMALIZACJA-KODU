import cv2
image_gray = cv2.imread("10648-orig.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("new_file_cat.jpg", image_gray)