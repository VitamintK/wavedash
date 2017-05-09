from pyo import *
s = Server(winhost="asio").boot()
s.start()
tab = SndTable(SNDS_PATH + '/transparent.aif')
pit = Choice(choice=[.5,.75,1,1.25,1.5], freq=[3,4])
start = Phasor(freq=.2, mul=tab.getDur())
dur = Choice(choice=[.0625,.125,.125,.25,.33], freq=4)
a = Looper(table=tab, pitch=pit, start=start, dur=dur, startfromloop=True, mul=.25).out()
