import pigpio

pi = pigpio.pi()

if not pi.connected:
	print('pigpio not connected')
	exit()

RED_PIN = 25
GREEN_PIN = 18
BLUE_PIN = 24

RESISTOR_PIN = 14

USED_PINS = [ RED_PIN, GREEN_PIN, BLUE_PIN ]

bright = 255


def setLights(pin, brightness):

	print('Setting pin {} with brightness {}'.format(pin, brightness))

	realBrightness = int(int(brightness) * (float(bright) / 255.0))
	pi.set_PWM_dutycycle(pin, realBrightness)


def embraceDarkness():
	for pin in USED_PINS:
		setLights(pin, 0)


def readResistor():
	return pi.read(RESISTOR_PIN)
