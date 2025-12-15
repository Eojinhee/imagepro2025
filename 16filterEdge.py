# filter -> edge

import cv2
import numpy as np

img = cv2.imread('./img/sudoku.jpg')

gx_kennel = np.array([[-1,1]])
gy_kennel = np.array([[-1],[1]])
edge_gx = cv2.filter2D(img,-1,gx_kennel)
edge_gy = cv2.filter2D(img,-1,gy_kennel)

cv2.imshow('org',img)
cv2.imshow('edge',edge_gx)
cv2.imshow('edge',edge_gy)
cv2.waitKey()
cv2.destroyAllWindows()

#sobel
gx_s = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
gy_s = np.array([[-1,2,-1],[0,0,0],[1,2,1]])
edge_gxs = cv2.filter2D(img,-1,gx_s)
edge_gys = cv2.filter2D(img,-1,gy_s)
edge_gxys = edge_gxs + edge_gys

sobelx = cv2.Sobel(img,-1,1,0,ksize=5)
cv2.imshow('org',img)
cv2.imshow('edge',edge_gx)
cv2.imshow('edge',edge_gy)
cv2.imshow('edgex sobel',sobelx)
cv2.imshow('edgey xys',edge_gxys)
cv2.waitKey()
cv2.destroyAllWindows()

#schar
gx_sh = np.array([[-3,0,3],[-10,0,10],[-3,0,3]])
gy_sh = np.array([[1,1,1],[1,1,1],[1,1,1]])
scharx = cv2.filter2D(img,-1,gx_sh)
schary = cv2.filter2D(img,-1,gy_sh)

#laplacian
gx_l = np.array([[0,1,0],[1,-4,1],[0,1,0]])
edge_lap = cv2.filter2D(img,-1,gx_l)

#canny
canny = cv2.Canny(img,50,150)

cv2.imshow('org',img)
cv2.imshow('scharx',scharx)
cv2.imshow('schary',schary)
cv2.imshow('lap',edge_lap)
cv2.imshow('canny',canny)
cv2.waitKey()
cv2.destroyAllWindows()


