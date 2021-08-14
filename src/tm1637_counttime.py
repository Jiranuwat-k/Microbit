from microbit import *
import tm1637
tm = tm1637.TM1637(clk=pin15,dio=pin16)
count =0
tm.show("")
while 1:
    btn = pin0.read_digital()
    sleep(100)
    if(btn == 0):
        count += 1
    else:
        count=count
    tm.show("%d"%(count))

