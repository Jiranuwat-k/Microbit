from microbit import *
Human = Image("00900:" 	
		     "99999:"
		     "00900:"
		     "09090:" 	
		     "90009")

count = 0
while 1:
    btn = pin0.read_digital()
    sleep(100)c
    if(btn == 0):
        count = count + 1
    elif(count > 4):
        count = 1
    if(count == 1):
        display.show(Image.HAPPY)
    elif(count == 2):
        display.show(Human)
    elif(count == 3):
        display.show(Image.PACMAN)
    elif(count == 4):
        display.show(Image.HEART)
