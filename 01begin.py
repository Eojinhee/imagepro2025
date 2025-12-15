import cv2

img_file = "./img/girl.jpg"
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow("IMG", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No img file')


from PIL import Image
Image.open('./img/boy_face.jpg').show()

img = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow("IMG", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('No img file')


video_file = "./img/big_buck.avi"
cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow("IMG", img)
            cv2.waitKey(25)
        else:
            break
else:
    print("cannot open video")

