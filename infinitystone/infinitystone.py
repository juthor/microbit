def on_button_pressed_a():
    global 인피티니스톤
    인피티니스톤 += 합
    basic.show_number(인피티니스톤)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global 합
    합 = randint(1, 6)
    if 합 == 1:
        strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    elif 합 == 2:
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
    elif 합 == 3:
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    elif 합 == 4:
        strip.show_color(neopixel.colors(NeoPixelColors.VIOLET))
    elif 합 == 5:
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif 합 == 6:
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_number(딱)
input.on_button_pressed(Button.B, on_button_pressed_b)

딱 = 0
합 = 0
인피티니스톤 = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB_RGB)
strip.clear()
strip.set_brightness(80)
strip.show()

def on_forever():
    global 딱
    딱 = pins.analog_read_pin(AnalogPin.P1)
    if 인피티니스톤 == 21 and 딱 > 200:
        strip.show_rainbow(1, 360)
        while 인피티니스톤 == 21:
            strip.rotate(1)
            strip.show()
            basic.pause(100)
basic.forever(on_forever)
