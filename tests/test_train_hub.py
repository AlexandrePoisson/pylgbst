from pylgbst.hub import TrainHub
from pylgbst import get_connection_gattool
from pylgbst.peripherals import Motor
import time

conn = get_connection_gattool(hub_mac='90:84:2B:0F:D1:F8') #auto connect does not work
hub = TrainHub(conn)

for device in hub.peripherals:
    print(device) 
hub._report_status()  
motor = Motor(hub, hub.PORT_A)
#hub.connection.notification_delayed('050082030a', 0.1)
motor.start_power(1.0) #here motor really moves
time.sleep(1)
#hub.connection.notification_delayed('050082030a', 0.1)
motor.stop() #here motor really stops
print("Goodbye")

"""
Output
Got only these devices: (Peripheral on port 0x0, None, None, LEDRGB on port 0x32, None, Current on port 0x3b, Voltage on port 0x3c)
0
50
59
60
Goodbye
"""