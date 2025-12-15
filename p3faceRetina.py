import cv2
from retinaface import RetinaFace

img_path = "./img/image.png"

faces = RetinaFace.detect_faces(img_path)
print(faces)

img = cv2.imread(img_path)
for key, face in faces.items():
    print(key)
    print(face)
    facial_area = face['facial_area']
    cv2.rectangle(img,(facial_area[0],facial_area[1]),
                  (facial_area[2],facial_area[3]),(255,0,0),2)
    print(facial_area)
    cv2.putText(img,f"{face['score']:.3f}",
                (facial_area[0],facial_area[1]),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0))
    cv2.putText(img,'woomin',(1300,80),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
# face1 = face['face_1']
# print(face1)
# facial_area = face1['facial_area']
# print(facial_area)

cv2.imshow('org',img)
cv2.waitKey()
cv2.destroyAllWindows()