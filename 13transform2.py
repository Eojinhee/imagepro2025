import cv2
import numpy as np

img = cv2.imread('./img/fish.jpg')
rows, cols,_ = img.shape

mtrx1 = np.float32([[-1,0,cols],[0,1,0]])
mtrx2 = np.float32([[1,0,0],[0,-1,rows]])
mtrx3 = np.float32([[-1,0,cols],[0,-1,rows]])

img1 = cv2.warpAffine(img,mtrx1,(rows,cols))
img2 = cv2.warpAffine(img,mtrx2,(rows,cols))
img3 = cv2.warpAffine(img,mtrx3,(rows,cols))

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()
cv2.destroyAllWindows()

#좌우반전
#for문
img_flipx = np.zeros_like(img)
for x in range(cols):
    for y in range(rows):
        img_flipx[y,x] = img[y,cols-x-1]

#배열연산
arr_flipx = np.zeros_like(img)
for x in range(cols):
    arr_flipx[:,x] = img[:,cols-x-1]

cv2.imshow('flip',img_flipx)
cv2.imshow('arr flip',arr_flipx)
cv2.imshow('org',img)
cv2.waitKey()
cv2.destroyAllWindows()