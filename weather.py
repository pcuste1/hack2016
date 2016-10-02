from urllib2 import Request, urlopen, URLError
import json
import thread

def input_thread(list):
    raw_input()
    list.append(None)

def do_stuff():
    list = []
    thread.start_new_thread(input_thread, (list,))
    while not list:
        stuff()
        
def main():
    #do_stuff()
    f = open("city.txt", 'r')
    name = "name"
    cities = {}
    while(name != ''):
        name = f.readline()
        if name != '':
            name = name.strip().split(',')
            cities[name[0].lower()] = [f.readline().strip(),f.readline().strip()]
    #print cities
    city = 'houston'
    while(city != "q"):
        city = raw_input("Please enter a city to look up (q to quit):").lower()
        if city != 'q':
            if city in cities:
                api = "https://api.darksky.net/forecast/d4cfdd96bee79c0f28e2ac13b2ee1172/"+cities[city][0]+","+cities[city][1]
                #print api
                request = Request(api)
                try:
                    response = urlopen(request)
                    weather = json.load(response)
                    print weather["currently"]
                except URLError, e:
                    print 'No kittez. Got an error code:', e
        else:
            print("Goodbye HackUMBC")
main()
