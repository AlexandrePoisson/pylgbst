from pylgbst.hub import TrainHub
from pylgbst import get_connection_gattool
from pylgbst.peripherals import Motor
import time

def callback(value):
    print("Voltage: %s" % value)



conn = get_connection_gattool(hub_mac='90:84:2B:0F:D1:F8') #auto connect does not work
hub = TrainHub(conn)

for device in hub.peripherals:
    print(device) 
motor = Motor(hub, hub.PORT_A)


#hub.connection.notification_delayed('050082030a', 0.1)
motor.start_power(1.0) #here motor really moves
time.sleep(0.5)
#hub.connection.notification_delayed('050082030a', 0.1)
motor.stop() #here motor really stops
print("Goodbye")

"""
Output
0
50  => 0x32
59  => 0x3B
60  => 0x3C
Goodbye
"""
