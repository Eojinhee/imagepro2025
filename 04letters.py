import cv2
import numpy as np
img = np.full((500, 500, 3), 255, dtype=np.uint8)



#sna-serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
#sna-serif normal
cv2.putText(img, "Simplex", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))
#sna-serif bold
cv2.putText(img, "Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
#sna-serif normal 크게
cv2.putText(img, "Simplex X 2", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0))


# serif small
cv2.putText(img, "Serif Plain", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0))
# serif normal
cv2.putText(img, "Serif normal", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
# serif bold
cv2.putText(img, "Serif bold", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0))
# serif normal X 2
cv2.putText(img, "Serif Plain X 2", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0, 0, 0))

# 한글표시
cv2.putText(img, "어진희제작", (50, 470), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

# freetype 객체 생성
ft2 = cv2.freetype.createFreeType2()

# 시스템 폰트 파일 불러오기 (예: 윈도우 맑은 고딕)
ft2.loadFontData(fontFileName="C:/Windows/Fonts/malgun.ttf", id=0)

# 한글 출력 (cv2.putText 대신 사용)
ft2.putText(img, "어진희제작", (50, 470), fontHeight=30, color=(0, 0, 255), thickness=-1, line_type=cv2.LINE_AA)


cv2.imshow("Girl", img)
cv2.waitKey()
cv2.destroyAllWindows()


