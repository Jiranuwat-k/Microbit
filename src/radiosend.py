# radio send
from microbit import *
import radio
radio.on()
radio.config(channel = 42)
radio.config(power=7)
msg = ""
while 1:
    temp = temperature()
    #msg = str(temp)
    print(msg)
    if msg != "":
        radio.send(hello)
    sleep(10)

