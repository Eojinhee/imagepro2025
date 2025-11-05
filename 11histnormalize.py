import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./img/yate.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])


# 이미지 노멀라이즈
#

#
# img_norm

# 형변환 유도
#img_norm = ((img - img.min()) / (img.max() - img.min()))


# 직접 형변환한 노멀라이즈
img_f = img.astype(np.float32)
img_norm = (img_f - img_f.min()) * 255 / (img_f.max() - img_f.min())
img_norm = img_norm.astype(np.uint8)

# opencv normalize
img_normcv = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

hist_norm = cv2.calcHist([img_norm], [0], None, [256], [0, 256])
hist_normcv = cv2.calcHist([img_normcv], [0], None, [256], [0, 256])

cv2.imshow('imgnorm', img_norm)
cv2.imshow('org', img)
cv2.imshow('normcv', img_normcv)
cv2.waitKey()
cv2.destroyAllWindows()

plt.subplot(1, 3, 1)
plt.plot(hist)
plt.subplot(1, 3, 2)
plt.plot(hist_norm)
plt.subplot(1, 3, 3)
plt.plot(hist_normcv)
plt.show()