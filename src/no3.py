from microbit import *
import neopixel
np = neopixel.NeoPixel(pin16,12)
"""
r = 0
g = 0
b = 0
btna = 0
pre_a = 0
mode = 0
"""
while 1:
    """
    if pin0.read_digital() == 1:
        if mode == 0:
            mode = 1
        if mode == 1:
            mode = 0
    print(mode)
    print(mode)
    sleep(100)
    """
    for i in range(0,12):
        np[i] = (0,0,255)
        np.show()
        sleep(100)
        np[i] = (0,0,0)
        np.show()
