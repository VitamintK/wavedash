from pyo import *
s = Server(winhost="asio").boot()
s.start()
t = HarmTable([1,0,.33,0,.2,0,.143,0,.111])
a = Osc(table=t, freq=[250,251], mul=.2).out()


def pat(args):
    base, ctr = args
    arp = [0,4,7,10,7,4]
    ctr[0]  = (ctr[0]+1)%len(arp)
    #f = random.randrange(200, 401, 25)
    f = base*pow(2,(arp[ctr[0]]/12.0))
    a.freq = [f, f+1]
p = Pattern(pat, .125, (330,[0]))
p.play()


if False:
    t = NewTable(length = 2, chnls = 1)
    a = Input(0)
    b = TableRec(a, t, 0.01)
    amp = Iter(b['trig'], [0.5])
    freq = t.getRate()
    c = Osc(t,[freq,freq*0.99],mul=amp).out()
