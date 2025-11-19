# 2025.11.19
# 이미지분석 -> 필터 -> 블러

import cv2
import numpy as np

img = cv2.imread('./img/girl.jpg')

kernel = np.ones((5, 5))/25
print(kernel)
blurred = cv2.filter2D(img, -1, kernel)
cv2.imshow('org', img)
cv2.imshow('blurred', blurred)
cv2.waitKey()
cv2.destroyAllWindows()

