import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./img/mountain.jpg',cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([img],[0],None,[256],[0,255])
plt.plot(hist)
plt.show()
print(hist.shape)
cv2.imshow('org',img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('./img/mountain.jpg')
channel = cv2.split(img)
colors = ('b', 'g', 'r')
for(ch, color) in zip(channel, colors):
    print(ch)
    print(color)
    hist = cv2.calcHist([ch],[0],None,[256],[0,255])
    plt.plot(hist,color=color)
plt.show()
