# Import standard python modules.
import sys
import time
import random
# This example uses the MQTTClient instead of the REST client
from Adafruit_IO import MQTTClient
import Adafruit_DHT
import RPi.GPIO as GPIO
pin = 21

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_isYZ61L05ONok0ht1pQ4cSvJmP5s'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'amit24'

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'led'
l1 = 20
l2 = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
sensor = Adafruit_DHT.DHT11

# called when we're connected to adafruit mqtt server
def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes.  The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format(FEED_ID))
    client.subscribe("led1")
    client.subscribe("led2")
    print('Waiting for feed data...')

#this function will be automatically called, if we're disconnected from adafruit mqtt server
def disconnected(client):
    """Disconnected function will be called when the client disconnects."""
    sys.exit(1)

# this function will be called whenever there is a new data to the feeds to which we've subscribed
def message(client, feed_id, payload):
    """Message function will be called when a subscribed feed has a new value.
    The feed_id parameter identifies the feed, and the payload parameter has
    the new value.
    """
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    print("Actual payload is ",payload)
    if feed_id == 'led1':
        if payload == 'ON':
            print("turn on LED 1 here")
            GPIO.output(l1,True)
        if payload == 'OFF':
            print("turn Off LED 1 here")
            GPIO.output(l1,False)
            
    if feed_id == 'led2':
        if payload == 'ON':
            print("turn on LED 2 here")
            GPIO.output(l2,True)
        if payload == 'OFF':
            print("turn Off LED 2 here")
            GPIO.output(l2,False)


# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

# Connect to the Adafruit IO server.
client.connect()

# The first option is to run a thread in the background so you can continue
# doing things in your program, to do so use below line
client.loop_background()


# Alternatively, you can simply block your program for waiting for incoming stream of
# data from subscription and the message function will take care of stuffs
#client.loop_blocking()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0}*C  Humidity={1}%'.format(temperature, humidity))
        client.publish('temp',temperature)
        client.publish('hum',humidity)
        print("values published")
        time.sleep(60)
    else:
        print('Failed to get reading. Try again!')
    

    

