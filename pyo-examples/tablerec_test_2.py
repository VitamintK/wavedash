from pyo import *
if len(sys.argv) > 1:
    #asio
    s = Server(winhost=sys.argv[1]).boot()
else:
    s = Server().boot()

s.start()


t = NewTable(length=2, chnls=1)
a = Input(0)
b = TableRec(a, t, .01)
amp = Iter(b["trig"], [.5, .2, .1, 0])
freq = t.getRate()
c = Osc(t, [freq, freq*.99], mul=amp).out()
# to record in the empty table, call:
# b.play()
def pat():
    print(amp.get())
    
p = Pattern(pat, 1)
p.play()
