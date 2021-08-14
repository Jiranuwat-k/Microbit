# radio read
from microbit import *
import radio
radio.on()
radio.config(channel = 42)
radio.config(power = 7)
data = ""
while 1:
    data = radio.receive()
    print(x)
    sleep(10)
