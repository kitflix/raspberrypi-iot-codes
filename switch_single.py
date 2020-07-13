import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #connect switch across VCC



while True:
    if GPIO.input(21) == True:
        print("Pin 21 is HIGH")
        time.sleep(1)
    else:
        print("Pin 21 is LOW")
        time.sleep(1)
