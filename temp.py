# if a physical sense hat is present, use below line
from sense_hat import SenseHat

#if a sense hat is not present and you wish to use emulator, then use this line
#from sense_emu import SenseHat

import time
from urllib.request import urlopen
sense = SenseHat()
url = "https://api.thingspeak.com/update?api_key=XVYVRV5TH5GN8P72&"

while True:# since true is written, the loop never stops, it executes indefinitely
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    humidity = round(humidity,1)
    temp = round(temp,2)
    pressure = round(pressure,2)
    print("temp = ",temp)
    print("Humidity = ",humidity)
    print("pressure = ",pressure)
    url_new = url + "field1=" + str(temp) + "&field2=" + str(humidity) + "&field3=" + str(pressure)
    print(url_new)
    html = urlopen(url_new)
    print(html.code)#http response code
    time.sleep(15)
