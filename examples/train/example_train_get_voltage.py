from pylgbst.hub import TrainHub, Voltage
from pylgbst import get_connection_gattool
from pylgbst.peripherals import Motor
import time

def callback(value):
    print("Voltage: %s" % value)


conn = get_connection_gattool(hub_mac='90:84:2B:0F:D1:F8') #auto connect does not work
hub = TrainHub(conn)

print ("Value L: " % hub.voltage.get_sensor_data(Voltage.VOLTAGE_L))
print ("Value S: " % hub.voltage.get_sensor_data(Voltage.VOLTAGE_S))

print("Goodbye")
