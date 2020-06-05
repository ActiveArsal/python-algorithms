# Class Library
import time 

# 3rd Party module
from bluetooth.ble import BeaconService

service = BeaconService() #<-- Creating an instance object of the class library

service.start_advertising("1111111-2222-3333-4444-555555555555555", 1, 1, 1, 200) #<--- Advertise the UUID and different ports

time.sleep(15)
service.stop_advertise()

print("Done.")

