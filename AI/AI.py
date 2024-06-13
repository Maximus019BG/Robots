huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_COLOR_RECOGNITION)

def on_forever():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        basic.show_icon(IconNames.HEART)
    if huskylens.is_appear(2, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
