input.onButtonPressed(Button.A, function () {
    인피티니스톤 += 합
    basic.showNumber(인피티니스톤)
})
input.onGesture(Gesture.Shake, function () {
    합 = randint(1, 6)
    if (합 == 1) {
        strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    } else if (합 == 2) {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
    } else if (합 == 3) {
        strip.showColor(neopixel.colors(NeoPixelColors.Orange))
    } else if (합 == 4) {
        strip.showColor(neopixel.colors(NeoPixelColors.Violet))
    } else if (합 == 5) {
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
    } else if (합 == 6) {
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(딱)
})
let 딱 = 0
let 합 = 0
let 인피티니스톤 = 0
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB_RGB)
strip.clear()
strip.setBrightness(80)
strip.show()
basic.forever(function () {
    딱 = pins.analogReadPin(AnalogPin.P1)
    if (인피티니스톤 == 21 && 딱 > 200) {
        strip.showRainbow(1, 360)
        while (인피티니스톤 == 21) {
            strip.rotate(1)
            strip.show()
            basic.pause(100)
        }
    }
})
