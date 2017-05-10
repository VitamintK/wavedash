from pyo import *
s = Server(duplex=1, winhost='asio').boot()
s.start()
t = NewTable(length = 2, chnls = 1)
a = Input(0)
b = TableRec(a, t, 0.01)
amp = Iter(b['trig'], [0.5])
freq = t.getRate()
c = Osc(t,[freq,freq*0.99],mul=amp).out()
