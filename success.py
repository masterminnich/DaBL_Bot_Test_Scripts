import ssl
import re
from pyfirmata import Arduino, util
import time

board = Arduino("/dev/cu.usbmodem3827781")

while True:
	board.digital[12].write(1)
	time.sleep(.5)
	board.digital[12].write(0)
	time.sleep(.2)