from pyo import *
s = Server().boot()
# Sets fundamental frequency.
freq = 200

# LFO applied to the `sharp` attribute
lfo = Sine(.2, mul=0.5, add=0.5)

# Various band-limited waveforms
osc = LFO(freq=freq, sharp=lfo, mul=0.4).out()
osc.ctrl()

# Displays the waveform
sc = Scope(osc)

# Displays the spectrum contents
sp = Spectrum(osc)

s.gui(locals())