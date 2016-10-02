from urllib2 import Request, urlopen, URLError
import json
import thread

import numpy as np
import cv2
import thread

#This creates the cities repository that we use to determine latitude and longitude 
f = open("city.txt", 'r')
name = "name"
cities = {}
while(name != ''):
    # each city in city.txt takes 3 lines worth of data. the first is the name followed by lat and long
    name = f.readline()
    if name != '':
        name = name.strip().split(',')
        cities[name[0].lower()] = [f.readline().strip(),f.readline().strip()]

# This gets input from the user and then appends it to a list. Useful for threading
def input_thread(a):
    #print cities
    city = 'houston'
    city = raw_input("Please enter a city to look up:").lower()
    choice = ''
    # for testing purposes
    if city == 'rain':
        a.append(city)
        return
    elif (city == 'clear-day'):
        a.append(city)
        return
    elif (city == 'clear-night'):
        a.append(city)
        return
    elif (city == 'snow'):
        a.append(city)
        return
    elif (city == 'thunderstorm'):
        a.append(city)
        return
    elif (city == 'wind'):
        a.append(city)
        return
    elif (city == 'fog'):
        a.append(city)
        return
    elif (city == 'cloudy' or city == 'partly-cloudy-day'):
        a.append(city)
        return
    elif (city == 'tornado'):
        a.append(city)
        return
                
    #checks if the user input is in cities. if not, loops
    while city not in cities:
        print "Not a city, please try again."
        city = raw_input("Please enter a city to look up:").lower()
    api = "https://api.darksky.net/forecast/d4cfdd96bee79c0f28e2ac13b2ee1172/"+cities[city][0]+","+cities[city][1]
    #print api
    # this gets the current weather condition in the chosen city
    request = Request(api)
    try:
        response = urlopen(request)
        weather = json.load(response)
        choice = weather["currently"]["icon"]
    except URLError, e:
        print 'No kittez. Got an error code:', e
    #appends the weather condition to list a. For a thread this breaks it out of the loop.
    print choice
    a.append(choice)
    
def main():
    cv2.namedWindow("main",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("main",600,400)
    cv2.moveWindow("main",0,0)
    a = []
    input_thread(a)
    num = a[0]
    while(1):
        # all the different video choices based on weather conditions
        if (num == 'rain'):
            video = 'rain.avi'
        elif (num == 'clear-day'):
            video = 'clear_day.avi'
        elif (num == 'clear-night'):
            video = 'clear_night.avi'
        elif (num == 'snow'):
            video = 'snow.avi'
        elif (num == 'thunderstorm'):
            video = 'thunderstorm.avi'
        elif (num == 'wind'):
            video = 'windy.avi'
        elif (num == 'fog'):
            video = 'fog.avi'
        elif (num == 'cloudy' or num == 'partly-cloudy-day'):
            video = 'cloud.avi'
        elif (num == 'tornado'):
            video = 'turnado.avi'
        else:
            video = 'earth.avi'
        # Capture video from file
        cap = cv2.VideoCapture(video)
        frame_counter = 0
        a = []
        # starts a new input thread
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
