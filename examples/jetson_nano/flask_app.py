from flask import Flask, request, redirect, url_for, render_template, json, render_template_string, jsonify

from pylgbst.hub import TechnicHub
from pylgbst import get_connection_gattool
from pylgbst.peripherals import Motor,EncodedMotor
import time

app = Flask(__name__)

conn = ''
hub = ''
power_direction =''
power_motor =''
@app.route('/', methods=['GET', 'POST'])
def control_panel():
    global conn
    global hub
    global power_direction
    global power_motor    
    print('request.form:', request.form)
    
    if request.method == 'POST':
        if request.form.get('button') == 'button-play':
            conn = get_connection_gattool(hub_mac='90:84:2B:5F:33:35') #auto connect does not work
            hub = TechnicHub(conn)
            power_direction = EncodedMotor(hub, hub.PORT_B)
            power_motor = EncodedMotor(hub, hub.PORT_D)
            print("play button pressed")

        elif request.form.get('button') == 'button-exit':
            power_motor.stop()
            power_direction.stop()
            conn.disconnect() 
            print("exit button pressed")


        elif request.form.get('slide_direction') or request.form.get('slide_power'):
            direction = request.form.get('slide_direction')
            power = request.form.get('slide_power')
            power_motor.start_power(float(power)/100)
            power_direction.start_power(float(direction)/100)
            print('print direction:', direction,'print power:', power)
            #return json.dumps({'direction': direction,'power': power})

    return render_template('main.html')

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True, use_reloader=False)
