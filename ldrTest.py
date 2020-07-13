import RPi.GPIO as GPIO
import time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
GPIO.setmode(GPIO.BCM)
pin=21
while True:
    reading=0
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    GPIO.setup(pin,GPIO.IN)
    while(GPIO.input(pin)==GPIO.LOW):
        reading = reading + 1
    print (reading)
    time.sleep(1)


