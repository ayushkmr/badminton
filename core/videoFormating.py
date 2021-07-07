import cv2

def videoDetails(location, lines):
    cap = cv2.VideoCapture(location)
    object_detector = cv2.createBackgroundSubtractorMOG2(history = 60, varThreshold = 55, detectShadows = False)
    _, frame = cap.read()
    while True:
        _, frame = cap.read()        
        mask = blurrImages(frame,object_detector)     
        cnt = trackObject(mask,frame)      
        
        for line in lines:
            cv2.line(mask, (int(line[0]),int(line[1])), (int(line[2]),int(line[3])), (255,255,255),2)

        cv2.imshow("mask", mask)
        cv2.imshow("frame", cnt)
        
        key = cv2.waitKey(1)        
        if key == ord('q'):
            break
        
    cv2.destroyAllWindows()
    cap.release()


def blurrImages(frame,object_detector):
    
    mask = object_detector.apply(frame)
    mask = cv2.GaussianBlur(mask,(3,3), 0)
    _, mask = cv2.threshold(mask,254,255, cv2.THRESH_BINARY)
    return mask
    

def trackObject(mask, frame):
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 10 and area >5:
            (x,y,w,h) = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)
            cv2.putText(frame, str(len(approx)), (x+w+10,y+h+10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (130,255,255),2)

    return frame


def showImage():
    pass