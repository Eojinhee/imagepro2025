import cv2

# 이미지 파일 읽기
img_file = "./img/girl.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')

# 2025.9.17 pillow를 사용한 이미지 보기
from PIL import Image
img = Image.open("./img/girl.jpg")
img.show()

img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No image file.')

# 동영상파일 읽기
video_file = "./img/big_buck.avi"

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break
else:
    print("can't open video.")
cap.release()
cv2.destroyAllWindows()

# 비디오카메라 읽기
cap = cv2.VideoCapture(0)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame')
            break
else:
    print("can't open camera.")
cap.release()
cv2.destroyAllWindows()

# 사진찍기
cap = cv2.VideoCapture(0)
if cap.isOpened() :
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera',frame)
            if cv2.waitKey(1) != -1:
                cv2.imwrite('./img/photo.jpg', frame)
                break
        else:
            print('no frame!')
            break
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()
