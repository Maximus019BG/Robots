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
def forward(time3: number):
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 236)
    control.wait_micros(time3 * 1000000)
    maqueen.motor_stop(maqueen.Motors.ALL)
basic.show_icon(IconNames.PITCHFORK)
forward(2)
rightTurn(0.6)
forward(1)
control.wait_micros(5 * 1000000)
forward(1)
leftTurn(0.6)
forward(1)
leftTurn(0.6)
forward(0.5)

def on_forever():
    pass
basic.forever(on_forever)
