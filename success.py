import ssl
import re
from pyfirmata import Arduino, util
import time

board = Arduino("/dev/ttyACM0")

while True:
    board.digital[15].write(1)
    time.sleep(.5)
    board.digital[15].write(0)
    time.sleep(.2)
