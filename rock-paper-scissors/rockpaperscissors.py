TEMP = 0

def on_gesture_shake():
    global TEMP
    TEMP = randint(0, 2)
    if TEMP == 0:
        basic.show_icon(IconNames.SCISSORS)
    elif TEMP == 1:
        basic.show_leds("""
            . . . . .
            # # # # #
            # . # . #
            # # # # #
            . . . . .
            """)
    else:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
