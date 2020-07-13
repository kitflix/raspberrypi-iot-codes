# Import standard python modules.
import sys
import time
import random
# This example uses the MQTTClient instead of the REST client
from Adafruit_IO import MQTTClient

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_isYZ61L05ONok0ht1pQ4cSvJmP5s'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'amit24'

# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'led'

# called when we're connected to adafruit mqtt server
def connected(client):
    """Connected function will be called when the client is connected to
    Adafruit IO.This is a good place to subscribe to feed changes.  The client
    parameter passed to this function is the Adafruit IO MQTT client so you
    can make calls against it easily.
    """
    # Subscribe to changes on a feed named Counter.
    print('Subscribing to Feed {0}'.format(FEED_ID))
    client.subscribe(FEED_ID)
    client.subscribe("freq")
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
    if feed_id == 'led':
        if payload == 'ON':
            print("turn on LED here")
        if payload == 'OFF':
            print("turn Off LED here")


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
    press = random.randint(10000,12000)
    client.publish('pressure',press)
    print("pressure published")
    time.sleep(45)

    

