import numpy as np
import cv2
import thread

def input_thread(a):
    num = int(raw_input())
    a.append(num)

cv2.namedWindow("main",cv2.WINDOW_NORMAL)
cv2.resizeWindow("main",600,400)
cv2.moveWindow("main",0,0)
a = []
num = int(input())
while(1):
    if (num == 1):
        video = 'night.avi'
    elif (num == 2):
        video = 'sun.avi'
    else:
        video = 'turnado.avi'

        # Capture video from file
    cap = cv2.VideoCapture(video)
    frame_counter = 0
    a = []
    thread.start_new(input_thread, (a,))
    while(cap.isOpened() and a == []):
        ret, frame = cap.read()
        frame_counter += 1
        if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                frame_counter = 0
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        cv2.imshow("main",frame)
        if cv2.waitKey(25) and 0xFF == ord('q'):
            break
    cap.release()
    num = a[0]
    a = []
cv2.destroyWindow()
    
