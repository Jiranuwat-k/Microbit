from microbit import *
import tm1637
tm = tm1637.TM1637(clk=pin15,dio=pin16)
tm.show("0000")
while 1:
    btn = pin0.read_analog()
    btn = int(btn/113)
    tm.show('{}{}{}{}'.format(btn,btn,btn,btn))
