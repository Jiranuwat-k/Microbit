
from microbit import*
while True:
    if button_a.was_pressed():
        speaker.on()
        display.show(Image.YES)
    if button_b.was_pressed():
        speaker.off()
        display.show(Image.NO)
    if pin_logo.is_touched():
        audio.play(Sound.HELLO)
        sleep(1000)
