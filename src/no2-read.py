from microbit import *
from ssd1306 import initialize,clear_oled
from ssd1306_text import add_text
import radio
initialize()
clear_oled()
radio.on()
radio.config(channel = 40)
radio.config(power = 7)
dat = ""
data = ""
msg = ""
while 1:
    data = radio.receive()
    if data != None:
        if data == "e":
            clear_oled()
        else:
            dat = list(data)
            msg = data.split(dat[0])
            add_text(0,int(dat[0]),msg[1])
        display.show(data[0])
    sleep(10)
