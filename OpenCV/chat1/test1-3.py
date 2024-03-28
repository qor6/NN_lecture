import cv2 as cv
import sys

img = cv.imread('C://Users/win/Downloads/aie/apples.jpg')

if img is None : 
    sys.exit('no file')

cv.imshow('Image Display', img)
# (0,0)의 B,G,R
print(img[0,0,0], img[0,0,1], img[0,0,2])

cv.waitKey()
cv.destroyAllWindows()

print(type(img))
print(img.shape)