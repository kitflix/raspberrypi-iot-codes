from urllib.request import urlopen
import random
import time



url = "https://api.thingspeak.com/update?api_key=XVYVRV5TH5GN8P72&"

while True:
    temp = random.randint(20,40)
    humidity = random.randint(50,75)
    pressure = random.randint(10000,12000)
    url_new = url + "field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pressure)
    print(url_new)
    html = urlopen(url_new)
    print(html.code)#http response code
    time.sleep(15)
