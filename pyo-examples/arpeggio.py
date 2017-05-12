from pyo import *
s = Server(winhost="asio").boot()
s.start()
t = HarmTable([1,0,.33,0,.2,0,.143,0,.111])
a = Osc(table=t, freq=[250,251], mul=.2).out()

if False:
    #dominant 7 arpeggio
    def pat(args):
        base, ctr = args
        arp = [0,4,7,10,7,4,0,0,0,0,-1000,-1000]
        ctr[0]  = (ctr[0]+1)%len(arp)
        #f = random.randrange(200, 401, 25)
        f = base*pow(2,(arp[ctr[0]]/12.0))
        a.freq = [f, f+1]
    p = Pattern(pat, .2, (330,[0]))
    p.play()
if True:
    import random
    #meanderer
    def pat(args):
        markov = [[0.6,0.2,0.2],[0.4,0.4,0.2],[0.15,0.25,0.6]]
        base, direction = args
        #arp = [0,4,7,10,7,4,0,0,0,0,-1000,-1000]
        r = random.random()
        running_sum = 0.0
        for ind, i in enumerate(markov[direction[0]]):
            running_sum += i
            if running_sum >= r:
                direction[0] = ind-1
                break
        #ctr[0]  = (ctr[0]+1)%len(arp)
        #f = random.randrange(200, 401, 25)
        f = base[0]*pow(2,((4*direction[0])/12.0))
        base[0] = f
        a.freq = [f, f+1]
    p = Pattern(pat, .2, ([330],[0]))
    p.play()

if False:
    t = NewTable(length = 2, chnls = 1)
    a = Input(0)
    b = TableRec(a, t, 0.01)
    amp = Iter(b['trig'], [0.5])
    freq = t.getRate()
    c = Osc(t,[freq,freq*0.99],mul=amp).out()
