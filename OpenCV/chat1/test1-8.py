import cv2 as cv
import sys

img = cv.imread('C://Users/win/Downloads/aie/apples.jpg')

if img is None : 
    sys.exit('no file')

def draw(event, x, y, flags, param):    #콜백 함수
    if event==cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭 시
        cv.rectangle(img, (x,y),(x+200,y+200), (0,0,255),2)
    elif event==cv.EVENT_RBUTTONDOWN: # 마우스 오른쪽 버튼 클릭 시
         cv.rectangle(img, (x,y),(x+100,y+100), (255,0,0),2)
    
    cv.imshow("Drawing", img)
cv.namedWindow("Drawming")
cv.imshow("Drawing", img)
cv.setMouseCallback('Drawing', draw)    # drawing 윈도우에 draw 콜백 함수 지정

while(True):
    if cv.waitKey(1)==ord('q'): #end
        cv.destroyAllWindows()
        break