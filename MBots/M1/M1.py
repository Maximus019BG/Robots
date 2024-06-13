def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_icon(IconNames.HEART)
    elif receivedNumber == 1:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.NO)
radio.on_received_number(on_received_number)

def leftTurn(time: number):
    maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    control.wait_micros(time * 1000000)
    maqueen.motor_stop(maqueen.Motors.ALL)
def rightTurn(time2: number):
    maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    control.wait_micros(time2 * 1000000)
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.show_icon(IconNames.PITCHFORK)
def forward(time3: number):
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 236)
    control.wait_micros(time3 * 1000000)
    maqueen.motor_stop(maqueen.Motors.ALL)
radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
