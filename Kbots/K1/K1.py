def forward(distance: number):
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 105)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    control.wait_micros(distance * 1000000 / 16.8 )
    maqueen.motor_stop(maqueen.Motors.M1)
    maqueen.motor_stop(maqueen.Motors.M2)

def left_turn(degrees: number):
    maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    control.wait_micros(degrees * 1000000 / 100)
    maqueen.motor_stop(maqueen.Motors.M2)

def right_turn(degrees: number):
    maqueen.motor_stop(maqueen.Motors.ALL)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
    control.wait_micros(degrees * 1000000 / 100)
    maqueen.motor_stop(maqueen.Motors.M1)

def on_button_pressed_a():
    forward(35)
    left_turn(90)
    forward(35)
    maqueen.motor_stop(maqueen.Motors.ALL)

def on_button_pressed_b():
    forward(20)
    right_turn(90)
    forward(60)
    right_turn(90)
    forward(40)
    maqueen.motor_stop(maqueen.Motors.ALL)

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)