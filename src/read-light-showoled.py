from microbit import *
from ssd1306 import initialize,clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()
x=0
st='cnt='
while 1:
    y= str(display.read_light_level())
    add_text(0,2,y)
    x=x+1
    sleep(200)

