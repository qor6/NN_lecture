import cv2 as cv
import sys

img = cv.imread('C://Users/win/Downloads/aie/apples.jpg')

if img is None : 
    sys.exit('no file')

def draw(event, x, y, flags, param):    #콜백 함수
    global ix,iy

    if event==cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭 시 초기 위치 저장
        ix, iy = x, y
    elif event==cv.EVENT_RBUTTONDOWN: # 마우스 오른쪽 버튼 클릭시 직사각형 그리기
         cv.rectangle(img, (ix,iy),(x,y), (0,0,255),2)
    
    cv.imshow("Drawing", img)
    
cv.namedWindow("Drawming")
cv.imshow("Drawing", img)
cv.setMouseCallback('Drawing', draw)    # drawing 윈도우에 draw 콜백 함수 지정

while(True):
    if cv.waitKey(1)==ord('q'): #end
        cv.destroyAllWindows()
        break