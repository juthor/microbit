def on_button_pressed_a():
    global 숫자
    숫자 += 1
    basic.show_number(숫자)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global 숫자
    숫자 = 0
    basic.show_number(숫자)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 숫자
    숫자 += -1
    basic.show_number(숫자)
input.on_button_pressed(Button.B, on_button_pressed_b)

숫자 = 0
숫자 = 0