import cv2
import numpy as np
img = cv2.imread('lena.jpg')
rows, cols = img.shape[:2]

mtrx = np.float32([[1, 0, 100],
                   [0, 1, 100]])

mtrx2 = np.float32([[1, 0, -100],
                    [0, 1, -100]])

mtrx2 = np.float32([[1, 0, 100],
                    [0, 1, -100]])

img1 = cv2.warpAffine(img, mtrx, (cols, rows))

cv2.imshow('img1', img1)
cv2.waitKey()
cv2.destroyAllWindows()

