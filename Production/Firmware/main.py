import board
import busio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap



keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)



i2c = busio.I2C(board.D5, board.D4)

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.text("INFINITE PAD", 0, 0, 1)
oled.text("READY", 0, 16, 1)
oled.show()




keyboard.row_pins = (
    board.D0,
    board.D1,
    board.D2, 
)

keyboard.col_pins = (
    board.D6,
    board.D7,
    board.D8,
    board.D9,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW




FILE_EXPLORER = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.E),
    Release(KC.LGUI),
)

CLOSE_WINDOW = KC.MACRO(
    Press(KC.LALT),
    Tap(KC.F4),
    Release(KC.LALT),
)

ALT_TAB = KC.MACRO(
    Press(KC.LALT),
    Tap(KC.TAB),
    Release(KC.LALT),
)

NEXT_DESKTOP = KC.MACRO(
    Press(KC.LCTRL),
    Press(KC.LGUI),
    Tap(KC.RIGHT),
    Release(KC.LGUI),
    Release(KC.LCTRL),
)


MUTE_UNMUTE = KC.MUTE




keyboard.keymap = [
    [
        NEXT_DESKTOP,       # K1
        KC.R,               # K2
        MUTE_UNMUTE,        # K3
        KC.T,               # K4

        FILE_EXPLORER,      # K5
        KC.LGUI,             # K6
        KC.ENTER,            # K7
        KC.N8,               # K8

        KC.N9,               # K9
        CLOSE_WINDOW,        # K10
        ALT_TAB,             # K11
        KC.E,                # K12
    ]
]



if __name__ == '__main__':
    keyboard.go()

