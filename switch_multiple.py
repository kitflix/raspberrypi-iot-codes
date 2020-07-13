import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(21) == True:
        print("Pin 21 is HIGH")
        time.sleep(1)
    else:
        print("Pin 21 is LOW")
        time.sleep(1)
        
    if GPIO.input(20) == True:
        print("pin 20 is high")
        time.sleep(1)
    else:
        print("Pin 20 is low")
        time.sleep(1)
