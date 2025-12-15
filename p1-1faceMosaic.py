import cv2

face_cascade = cv2.CascadeClassifier('./recdata/haarcascade_frontalface_default.xml')

img = cv2.imread('./img/image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)
print(faces)

eye_cascade = cv2.CascadeClassifier('./recdata/haarcascade_eye.xml')


#cv2.rectangle(img,(146,96),(120+146,120+96),(255,0,0),5)
#cv2.rectangle(img,(398,97),(106+398,106+97),(0,255,0),5)
#cv2.rectangle(img,(146,96),(146+306,190+306),(0,255,0),5)

for face in faces:
    fx,fy,fw,fh = face
    roi = img[fy:fy + fh, fx:fx + fw]
    roi = cv2.resize(roi,(fw//10,fh//10))
    roi = cv2.resize(roi,(fw,fh))
    img[fy:fy + fh, fx:fx + fw] = roi

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
