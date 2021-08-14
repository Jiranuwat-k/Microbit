from microbit import *
x = 2
y = 2
dis = []
pin0.set_touch_mode(pin0.CAPACITIVE)
pin1.set_touch_mode(pin1.CAPACITIVE)
pin2.set_touch_mode(pin2.CAPACITIVE)
def cerser(x,y,set_p):
    if set_p == 0:
        display.set_pixel(x,y,9)
        sleep(50)
        display.set_pixel(x,y,0)
        sleep(50)
    elif set_p == 1:
        display.set_pixel(x,y,9)
while 1:
    if pin0.is_touched():
        cerser(x,y,1)
    elif pin1.is_touched():
        display.set_pixel(x,y,0)
    if button_a.get_presses():
        x -= 1
    elif button_b.get_presses():
        x += 1
    elif pin_logo.is_touched():
        y -= 1
    elif pin2.is_touched():
        y += 1
    if x > 4 :
        x = 4
    elif x < 0:
        x = 0
    elif y > 4:
        y = 4
    elif y < 0:
        y = 0
    elif accelerometer.is_gesture('shake'):
        display.clear()
    cerser(x,y,0)


