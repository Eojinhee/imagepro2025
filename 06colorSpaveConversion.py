import cv2
import numpy as np

img_file = './img/girl.jpg'
img = cv2.imread(img_file)
print(img.shape)

imgy = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
y,u,v = cv2.split(imgy)

cv2.imshow('girl',img)
cv2.imshow('imgy',y)
cv2.waitKey()
cv2.destroyAllWindows()

imgyy = np.full((293,406),255,dtype=np.uint8)
b,g,r = cv2.split(imgy)
imgyy = 0.299 * r + 0.587 * g + 0.114 * b
imgyy = imgyy.astype(np.uint8)

diff = y - imgyy

print(diff)