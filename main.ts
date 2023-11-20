input.onPinPressed(TouchPin.P0, function () {
    music.play(music.stringPlayable("B A G A G F A C5 ", 199), music.PlaybackMode.LoopingInBackground)
})
input.onButtonPressed(Button.A, function () {
    music.play(music.stringPlayable("- - - - - - - - ", 120), music.PlaybackMode.LoopingInBackground)
    music.play(music.stringPlayable("- - - - - - - - ", 0), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Whole)), music.PlaybackMode.LoopingInBackground)
})
input.onPinPressed(TouchPin.P2, function () {
    record.startRecording(record.BlockingState.Nonblocking)
})
function doSomething (image: Image, text: string, bool: boolean, list: any[]) {
	
}
input.onPinPressed(TouchPin.P1, function () {
    music.play(music.createSoundExpression(WaveShape.Noise, 500, 499, 255, 0, 5000, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.LoopingInBackground)
})
