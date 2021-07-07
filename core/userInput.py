import numpy as np
import cv2
import core.videoFormating as format

poly = []
rect = (0,0,0,0)
start=False
end = False
count = 0

def on_mouse(event, x, y, flags, params):
    global rect,start,end,count
    count+=1
    if event == cv2.EVENT_LBUTTONDOWN and  start == False:
        # print("click")
        start = True
        rect = (x,y,0,0)
        
    elif event == cv2.EVENT_LBUTTONUP and end == False:
        # print("lift")
        end = True
        rect = (rect[0],rect[1],x,y)


def setBoundaries(location, lines, timeSkip):
    cap = cv2.VideoCapture(location)
    ret, frame = cap.read()
    for i in range(int(timeSkip)):
        ret, frame = cap.read()

    mask = cv2.GaussianBlur(frame,(3,3), 0)
    canny = cv2.Canny(mask,25,90)
    cv2.imshow("Boundary",canny)

    for i in range(int(lines)):
        global count,start,end
        count=0
        start = False
        end = False
        if count <2 :
            cv2.setMouseCallback("Boundary",on_mouse)
            key = cv2.waitKey(0)
            poly.append(rect)
            # print(rect)

    processVideo(location)


def generateLines(image):
    mask = cv2.GaussianBlur(image,(5,5), 0)
    canny = cv2.Canny(mask,80,100)
    lines = cv2.HoughLinesP(canny,1,np.pi/180,100, np.array([]), minLineLength=120, maxLineGap =13)
    return lines


def processVideo(location):
    format.videoDetails(location, poly)