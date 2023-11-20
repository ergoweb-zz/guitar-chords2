def on_pin_pressed_p0():
    music.play(music.string_playable("B A G A G F A C5 ", 199),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    music.play(music.string_playable("- - - - - - - - ", 120),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    music.play(music.string_playable("", 0),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(659, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    music._play_default_background(music.built_in_playable_melody(Melodies.WEDDING),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p1():
    music.play(music.create_sound_expression(WaveShape.NOISE,
            500,
            499,
            255,
            0,
            5000,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
