# 2025.10.15
# 이미지분석 수업: threshold
# threshold:  문턱값

import cv2
import numpy as np


img = cv2.imread('./img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)
thresh_np = np.zeros_like(img)
# 중간숫자 : 127
# 첫번째방법
thresh_np[img > 192] = 255
thresh_np[(img > 128) & (img <= 192) ]  =128
thresh_np[(img > 64) & (img <= 128) ]  = 64

# 두번째방법
thresh_np = np.zeros_like(img)
thresh_np[img > 64] = 64
thresh_np[img > 128] = 128
thresh_np[img > 192] = 255

# 세번째 방법
thresh_np = np.zeros_like(img)
print(img.shape)
ysize, xsize = img.shape
for x in range(xsize):
    for y in range(ysize):
        if(img[y, x] > 64):
            thresh_np[y, x] = 64
        if (img[y, x] > 128):
            thresh_np[y, x] = 128
        if (img[y, x] > 192):
            thresh_np[y, x] = 255

_, thresh_cv =  cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh_np', thresh_np)
cv2.imshow("original", img)
cv2.imshow('cv thresh', thresh_cv)
cv2.waitKey()
cv2.destroyAllWindows()

# 실전에 적용 binary threshold
img = cv2.imread('./img/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)
_, thresh_cv80 =  cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, thresh_cv100 =  cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, thresh_cv120 =  cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
_, thresh_cv140 =  cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
t, thresh_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow('cv thresh80', thresh_cv80)
cv2.imshow('cv thresh100', thresh_cv100)
cv2.imshow('cv thresh120', thresh_cv120)
cv2.imshow('cv thresh140', thresh_cv140)
cv2.imshow('cv otsu', thresh_otsu)
cv2.imshow('paper', img)
print(f'{t=}')
cv2.waitKey()
cv2.destroyAllWindows()