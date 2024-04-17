import cv2 as cv
import sys

BrushSize = 5
LColor, RColor = (255,0,0), (0,0,255)

img = cv.imread('C://Users/win/Downloads/aie/apples.jpg')

if img is None:
    sys.exit("No file")

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x,y), BrushSize, RColor, -1)    
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x,y), BrushSize, LColor, -1)  
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x,y), BrushSize, RColor, -1)  
    cv.imshow("painting", img)

cv.namedWindow("painting")
cv.imshow("painting", img)
cv.setMouseCallback('painting', painting)

while(True):
    if cv.waitKey(1)==ord('q'): #end
        cv.destroyAllWindows()
        break
