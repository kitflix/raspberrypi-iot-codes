import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led=21

GPIO.setup(led,GPIO.OUT)

while True: 
    GPIO.output(led,True)
    time.sleep(4)
    GPIO.output(led,False)
    time.sleep(2)
    