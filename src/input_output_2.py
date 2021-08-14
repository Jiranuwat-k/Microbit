from microbit import *
Human = Image("00900:" 	
		     "99999:"
		     "00900:"
		     "09090:" 	
		     "90009")
per = 0
while 1:
    vr = pin0.read_analog()
    per = int(vr/255)
    """
    0 = 0%
    1 = 25%
    2 = 50%
    3 = 75%
    4 = 100%
    """
    if per == 0:
        display.clear()
    elif per == 1:
        display.show(Image.HAPPY)
    elif per == 2:
        display.show(Human)
    elif per == 3:
        display.show(Image.PACMAN)
    elif per == 4:
        display.show(Image.HEART)
