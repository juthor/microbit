let TEMP = 0
input.onGesture(Gesture.Shake, function () {
    TEMP = randint(0, 2)
    if (TEMP == 0) {
        basic.showIcon(IconNames.Scissors)
    } else if (TEMP == 1) {
        basic.showLeds(`
            . . . . .
            # # # # #
            # . # . #
            # # # # #
            . . . . .
            `)
    } else {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    }
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
