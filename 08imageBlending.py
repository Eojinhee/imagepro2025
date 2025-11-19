import cv2
import numpy as np

img1 = cv2.imread('./img/wing_wall.jpg')
img2 = cv2.imread('./img/yate.jpg')

img3 = img1 + img2
img4 = cv2.add(img1, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('add', img3)
cv2.imshow('cvadd', img4)

cv2.waitKey()
cv2.destroyAllWindows()

alpha = 0.5
blended_img = img1 * alpha + img2 * (1 - alpha)
blended_img = blended_img.astype(np.uint8)

blended_img = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

cv2.imshow('blended', blended_img)
cv2.imshow('blendedvb', blended_cv)
cv2.waitKey()
cv2.destroyAllWindows()

win_name = 'blended'
cv2.imshow(win_name, blended_img)
cv2.waitKey()
def onChange(x):
    alpha = x / 100
    dst = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
    cv2.imshow(win_name, dst)

cv2.imshow(win_name, img1)
cv2.createTrackbar('fade',win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()