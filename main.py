import audioio
import board
import array
import time
import math

audio_pin = board.A0
sample_rate = 8000
note_pitch = 440
note_length = 1

length = sample_rate // note_pitch

sine_wave = array.array("h", [0] * length)

for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15))
    
dac = audioio.AudioOut(audio_pin)

sine_wave = audioio.RawSample(sine_wave)

dac.play(sine_wave, loop=True)
time.sleep(note_length)
dac.stop()