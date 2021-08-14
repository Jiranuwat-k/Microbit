from microbit import *
import tm1637
tm = tm1637.TM1637(clk=pin16,dio=pin15)
btna = 0
btnb = 0
password = [5,6,7,8]
in_password = [0,0,0,0]
while 1:
    vr = pin1.read_analog()
    in_pass = int(vr/113)

    if button_b.get_presses():
        btnb = 1

    if button_a.get_presses():
        btna += 1
    if btna > 3:
        btna = 0
    display.show(btna)
    if btnb == 1:
        if password == in_password :
            display.show(Image.YES)
            pin8.write_digital(1)
            print("plass")
        else:
            display.show(Image.NO)

    if btna == 0:
        in_password[0] = in_pass
        tm.show('{}{}{}{}'.format(in_password[3],in_password[2],in_password[1],in_password[0]))
    elif btna == 1:
        in_password[1] = in_pass
        tm.show('{}{}{}{}'.format(in_password[3],in_password[2],in_password[1],in_password[0]))
    elif btna == 2:
        in_password[2] = in_pass
        tm.show('{}{}{}{}'.format(in_password[3],in_password[2],in_password[1],in_password[0]))
    elif btna == 3:
        in_password[3] = in_pass
        tm.show('{}{}{}{}'.format(in_password[3],in_password[2],in_password[1],in_password[0]))
    else:
        in_password = in_password
    sleep(100)
