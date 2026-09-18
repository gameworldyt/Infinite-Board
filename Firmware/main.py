import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.matrix import MatrixScanner
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.row_pins = (board.D0, board.D1, board.D2)
keyboard.col_pins = (board.D6, board.D7, board.D8, board.D9)

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

Mute_Unmute = KC.MUTE

keyboard.keymap = [
    [
        NEXT_DESKTOP, KC.R, Mute_Unmute, KC.T,

        FILE_EXPLORER, KC.LGUI, KC.ENTER, KC.N8,
        KC.N9, CLOSE_WINDOW, ALT_TAB, KC.E,
    ]
]