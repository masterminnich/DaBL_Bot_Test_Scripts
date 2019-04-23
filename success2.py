import ssl
import re
from pyfirmata import Arduino, util
import time

board = Arduino("/dev/ttyAMC0") #change this guy

#define digital output pins
pin14 = board.get_pin(‘d:15:o’) #digital/analog : pinNumber : input/output/pwm

while True:
	pin14.write(1)
	time.sleep(.5)
	pin14.write(0)
	time.sleep(.2)
	#board.digital[15].write(1)
	#time.sleep(.5)
	#board.digital[15].write(0)
	#time.sleep(.2)