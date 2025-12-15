import cv2
import numpy as np

img = cv2.imread('./img/gray_gradient.jpg',cv2.IMREAD_GRAYSCALE)
thresh_np = np.zeros_like(img)

thresh_np[img > 192] = 255
thresh_np[(img > 128) & (img <= 192)] = 128
thresh_np[(img > 64) & (img <= 128)] = 64

thresh_np = np.zeros_like(img)
thresh_np[img > 64] = 64
thresh_np[img <= 128] = 128
thresh_np[img <= 192] = 192

thresh_np = np.zeros_like(img)
print(img.shape)
ysize,xsize = img.shape
for x in range(xsize):
    for y in range(ysize):
        if(img[y,x] > 64):
            thresh_np[y,x] = 64
        if(img[y,x] > 128):
            thresh_np[y,x] = 128
        if(img[y,x] > 192):
            thresh_np[y,x] = 255

_, thresh_cv = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

cv2.imshow('thresh_np',thresh_np)
cv2.imshow('original',img)
cv2.imshow('thresh_np',thresh_cv)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('./img/scaned_paper.jpg',cv2.IMREAD_GRAYSCALE)
_, thresh_cv80 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
_, thresh_cv100 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
_, thresh_cv120 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
_, thresh_cv140 = cv2.threshold(img,140,255,cv2.THRESH_BINARY)
t, thresh_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


cv2.imshow('thresh_cv80',thresh_cv80)
cv2.imshow('thresh_cv100',thresh_cv100)
cv2.imshow('thresh_cv120',thresh_cv120)
cv2.imshow('thresh_cv140',thresh_cv140)
cv2.imshow('thresh_otsu',thresh_otsu)
cv2.imshow('paper',img)
print(f'{t=}')
cv2.waitKey()
cv2.destroyAllWindows()

blk_size =9
C = 5
img = cv2.imread('./img/sudoku.jpg',cv2.IMREAD_GRAYSCALE)
t, thresh_otsu = cv2.threshold(img,-1,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
th2G = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,blk_size,C)
th2M = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blk_size,C)
print(f'{t=}')
cv2.imshow('img',img)
cv2.imshow('otsu',thresh_otsu)
cv2.imshow('th2G',th2G)
cv2.imshow('th2M',th2M)
cv2.waitKey()
cv2.destroyAllWindows()
