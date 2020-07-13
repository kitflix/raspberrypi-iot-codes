import bmpsensor
import time
while True:
    temp, pressure, altitude = bmpsensor.readBmp180()
    print("Temperature is ",temp)  # degC
    print("Pressure is ",pressure) # Pressure in Pa 
    print("Altitude is ",altitude) # Altitude in meters
    print("\n")
    time.sleep(2)