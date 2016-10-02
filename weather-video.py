from urllib2 import Request, urlopen, URLError
import json
import thread

import numpy as np
import cv2
import thread

f = open("city.txt", 'r')
name = "name"
cities = {}
while(name != ''):
    name = f.readline()
    if name != '':
        name = name.strip().split(',')
        cities[name[0].lower()] = [f.readline().strip(),f.readline().strip()]

def input_thread(a):
    #print cities
    city = 'houston'
    city = raw_input("Please enter a city to look up (q to quit):").lower()
    choice = 'base'
    if city in cities:
        api = "https://api.darksky.net/forecast/d4cfdd96bee79c0f28e2ac13b2ee1172/"+cities[city][0]+","+cities[city][1]
        #print api
        request = Request(api)
        try:
            response = urlopen(request)
            weather = json.load(response)
            choice = weather["currently"]["icon"]
        except URLError, e:
            print 'No kittez. Got an error code:', e
    a.append(choice)
    
def main():
    cv2.namedWindow("main",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("main",600,400)
    cv2.moveWindow("main",0,0)
    a = []
    input_thread(a)
    num = a[0]
    while(1):
        if (num == 'rain'):
            video = 'rain.avi'
        elif (num == 'clear-day'):
            video = 'sun.avi'
        elif (num == 'wind'):
            video = 'turnado.avi'
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
    
main()
