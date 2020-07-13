from sense_emu import SenseHat
import time
sense = SenseHat()

while True:# since true is written, the loop never stops, it executes indefinitely
    temp = sense.get_temperature()
    print(temp)
    time.sleep(1)
