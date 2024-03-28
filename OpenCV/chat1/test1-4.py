import cv2 as cv
import sys

img = cv.imread('C://Users/win/Downloads/aie/apples.jpg')

if img is None : 
    sys.exit('no file')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR 컬러 영상을 명암(gray) 영상으로 변환
gray_small=cv.resize(gray,dsize=(0,0),fx=0.5,fy=0.5) # 반으로 축소

cv.imwrite('apples_gray.jpg', gray) #영상을 파일에 저장
cv.imwrite('apples_gray_small.jpg', gray_small)

cv.imshow('color.jpg', img)
cv.imshow('gray.jpg', gray)
cv.imshow('gray_small.jpg', gray_small)

cv.waitKey()
cv.destroyAllWindows()