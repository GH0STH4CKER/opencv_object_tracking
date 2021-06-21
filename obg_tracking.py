from cv2 import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()

success,img = cap.read()
bbox = cv2.selectROI('Tracking',img,False)
initialize = tracker.init(img,bbox)

def draw_box(img,bbox) :
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,72),3,1)

while True :
    timer = cv2.getTickCount()
    success , img = cap.read() 
    success , bbox = tracker.update(img)   
    xx = 7
    yy = 15

    if success == True:
        draw_box(img,bbox)

        cv2.rectangle(img,(xx,yy),(xx+265,yy+80),(245,64,124),-1,1)
        cv2.putText(img,'Status : ',(20,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(207,191,19),2)
        cv2.putText(img,'Tracking....',(115,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(26,237,30),2)
    else :
        cv2.rectangle(img,(xx,yy),(xx+265,yy+80),(245,64,124),-1,1)
        cv2.putText(img,'Status : ',(20,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(207,191,19),2)
        cv2.putText(img,'Lost tracking',(115,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(7,7,217),2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,'FPS : ',(20,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(207,191,19),2)
    cv2.putText(img,str(int(fps)),(85,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(12,42,240),2)

    cv2.imshow('Tracking',img)
    if cv2.waitKey(1) & 0xff==ord('q') :
        break