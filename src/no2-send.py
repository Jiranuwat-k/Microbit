from microbit import *
import radio
radio.on()
radio.config(channel = 40)
radio.config(power=7)
msg = ""
l_msg = ""
while 1:
    print("Type Message ")
    msg = input()
    l_msg = list(msg)
    if msg != "":
        radio.send(msg)
        display.show(str(l_msg[0]))
    sleep(10)
