radio.set_group(1)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_COLOR_RECOGNITION)

def on_forever():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        radio.send_number(0)
        basic.show_icon(IconNames.HEART)
    if huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        radio.send_number(1)
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
