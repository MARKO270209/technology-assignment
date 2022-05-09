def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
                . # # # .
                . . # . .
                . . # . .
                . # . # .
    """)
    basic.show_leds("""
        # . . . #
                . # # # .
                . # # # .
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . # .
                . # . # .
                # # # # .
                . # . # .
                # . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_string("Hi my name is Marko")
basic.show_string("")
basic.show_string("I have a dog")
basic.show_string("his name is jerry")
basic.show_string("one day me and jerry went on for a walk")
basic.show_string("until we came across this man with a lightsaber in his back pocket")
basic.show_string("Marko needed to have a rest because ")

def on_forever():
    pass
basic.forever(on_forever)
