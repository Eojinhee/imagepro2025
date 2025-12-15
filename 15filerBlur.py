#이미지분석 -> 필터 -> 블러

import cv2
import numpy as np

img = cv2.imread('./img/gaussian_noise.jpg')

kelnel = np.ones((5,5))/25
k1 = np.array([[1,2,1],[2,4,2],[1,2,1]])/16
print(kelnel)
blured = cv2.filter2D(img, -1, kelnel)
gblured = cv2.filter2D(img, -1, k1)
cv2.imshow('org',img)
cv2.imshow('blur',blured)
cv2.imshow('gblured',gblured)
cv2.waitKey()
cv2.destroyAllWindows()

#이미지분석 -> 필터 -> 가우시안, 메디안 median

k2 = cv2.getGaussianKernel(3,0)
print(k2)
blur2 = cv2.filter2D(img, -1, k2*k2.T)
print(k2*k2.T)
blur3 = cv2.GaussianBlur(img,(3,3),0)
blur4 = cv2.medianBlur(img,5)

imgmerge = np.hstack((img, blur3, blur4))
cv2.imshow('all',imgmerge)
cv2.waitKey()
cv2.destroyAllWindows()