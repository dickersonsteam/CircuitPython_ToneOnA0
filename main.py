# This example program will make a single sound play out
# of the selected pin.
#
# The following are the default parameters for which pin
# the sound will come out of, sample rate, note pitch/frequency,
# and note duration in seconds.
#
# audio_pin = board.A0
# sample_rate = 8000
# note_pitch = 440
# note_length = 1
#
# This example makes use of print messages to help debug
# errors. As you make changes and then run your code, watch
# these messages to understand what is happening (or not happening).
# When you add features, add messages to help you debug your own
# code. Ultimately, these print messages do slow things down a bit,
# but they will make you life easier in the long run.

import audioio
import board
import array
import time
import math

# record current time
start_time_pgm = time.monotonic()

# for Feather M0 use A0 only
# for Feather M4 either A0 or A1 work
audio_pin = board.A0

# Sample rate roughly determines the quality of the sound.
# A larger number may sound better, but will take
# more processing time and memory.
sample_rate = 8000

# Set the pitch for the note you would like to play.
# http://pages.mtu.edu/~suits/notefreqs.html
note_pitch = 440

# Set how many seconds the note will last.
# Try 0.1 - 1.0 or any number.
note_length = 1

# Now you must "draw" the sound wave in memory.
# This will take more or less time depending on the
# frequency and sample_rate that you selected.
print("Generate sound wave.")
start_time_gen = time.monotonic()
length = sample_rate // note_pitch

sine_wave = array.array("h", [0] * length)

for i in range(length):
    sine_wave[i] = int(math.sin(math.pi * 2 * i / 18) * (2 ** 15))

time_to_completion = time.monotonic() - start_time_gen

print("Generating the sound wave took " + str(time_to_completion) + " seconds.")
    
# Now initialize you DAC (aka speaker pin)
print("Initialize DAC.")
dac = audioio.AudioOut(audio_pin)

# Convert the sine wave you generated earlier into a
# sample that can be used with the dac.
print("Converting to RawSample.")
sine_wave = audioio.RawSample(sine_wave)

# Play the sine wave on the dac and loop it for however
# many seconds you set with note_length.
print("Playing sound.")
dac.play(sine_wave, loop=True)
time.sleep(note_length)
dac.stop()

# Print program execution time
print("Program completed execution.")
time_to_completion = time.monotonic() - start_time_pgm
print("Execution took " + str(time_to_completion) + " seconds.")