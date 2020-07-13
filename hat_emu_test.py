from sense_emu import SenseHat
import time
sense = SenseHat()
sense.clear()

while True:
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    temperature = sense.get_temperature()
    print(temperature)
    print(humidity)
    print(pressure)
    time.sleep(1)
