from pylgbst.hub import TechnicHub
from pylgbst import get_connection_gattool
from pylgbst.peripherals import Motor,EncodedMotor
import time
import random

def callback(value):
    print("Voltage: %s" % value)



conn = get_connection_gattool(hub_mac='90:84:2B:5F:33:35') #auto connect does not work
hub = TechnicHub(conn)

for device in hub.peripherals:
    print(device) 
direction_motor = Motor(hub, hub.PORT_B)
power_motor = Motor(hub, hub.PORT_D)


while True:
    
    #hub.connection.notification_delayed('050082030a', 0.1)
    power_motor.start_power(random.uniform(0, 1.0)) #here motor really moves
    direction_motor.start_power(random.uniform(-0.2, 0.2)) #here motor really moves
    time.sleep(0.5)
    #hub.connection.notification_delayed('050082030a', 0.1)
    power_motor.stop() #here motor really stops

print("Goodbye")

"""
Output
0
50  => 0x32
59  => 0x3B
60  => 0x3C
Goodbye
"""
