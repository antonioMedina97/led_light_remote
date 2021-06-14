import socketio
import re, time
from light_manager import *

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})



@sio.event
def change_color(color_json):
    print(color_json)

    regex_test = re.search('^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$', color_json['color'])

    # If it is a valid color expression
    if not regex_test == '':
        turn_on_the_lights(color_json['color'])


@sio.event
def disconnect():
    print('disconnected from server')

@sio.event
def light_detector():
    new_state = readResistor()
    sio.emit('light_changed', {'light_state': new_state})

@sio.event
def switch_off():
    embraceDarkness()



def turn_on_the_lights(hex_color):

    hex_color_stripped = hex_color.lstrip('#')
    dec_color = {
        'red': int(hex_color_stripped[:2], 16),
        'green': int(hex_color_stripped[2:4], 16),
        'blue': int(hex_color_stripped[4:6], 16)
    }

    print('led on')

    print( dec_color)

    setLights(RED_PIN, dec_color['red'])
    setLights(GREEN_PIN, dec_color['green'])
    setLights(BLUE_PIN, dec_color['blue'])



sio.connect('http://antoniomedina.iesmarquesdecomares.org/')
sio.wait()
