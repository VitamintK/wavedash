from pyo import *
import sys
if len(sys.argv) > 1:
    #asio
    s = Server(winhost=sys.argv[1]).boot()
else:
    s = Server().boot()
    
freq = 200
#lfo = Sine(0.2, mul = 0.5, add=0.5)
#lfo = Sine(0.2, mul = 0.0, add=0.0)
osc_ = LFO(freq=freq,mul=0.9)

osc = Degrade(osc_, bitdepth=8).out()
#osc.ctrl()
#lfo.ctrl()
#sc = Scope(osc)
#sp = Spectrum(osc)
#s.gui(locals())
s.start()



import pygame

pygame.init()

#create clock (for framerating)
clk = pygame.time.Clock()

#grab joystick 0
if pygame.joystick.get_count() == 0:
    raise IOError("No joysticks detected")
joy = pygame.joystick.Joystick(0)
joy.init()

BASE = 0
def pat(args):
        base, ctr = args
        arp = [0,4,7,10,13]
        ctr[0]  = (ctr[0]+1)%len(arp)
        #f = random.randrange(200, 401, 25)
        print(ctr)
        f = BASE*pow(2,(arp[ctr[0]]/12.0))
        osc_.freq = [f, f+1]
p = Pattern(pat, 0.1, (330,[0]))
p.play()
osc.stop()
import math

buttons = {}
for b in range(joy.get_numbuttons()):
    pass

t = NewTable(length = 5, chnls = 1)
a = Input(0)
T = TableRec(a, t, 0.01)
amp = Iter(T['trig'], [0.5])
Freq = t.getRate()
c = Looper(t,1,dur=2,mul=amp)
pva = PVAnal(c, size=1024)
pvt = PVTranspose(pva, transpo=1)
pvs = PVSynth(pvt).out()
#p = Pattern(pat, .2, ([0],[0]))

recording = False
while True:
    #tix+=1
    pygame.event.pump()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            import sys
            sys.exit()

    x = joy.get_axis(0)
    y = joy.get_axis(1)
    x2 = joy.get_axis(3)
    y2 = joy.get_axis(2)
    l = joy.get_axis(4)
    r = joy.get_axis(5)
    #print(math.floor(x*40 + 60))
    #print(midiToHz(math.floor(x*40 + 60)))
    if True:
        for b in range(joy.get_numbuttons()):
                
                    #else:
                        #recording = False
                        
            if joy.get_button(b):
                        if b == 2:
                            if not recording:
                                recording = True
                                T.play()
                            else:
                                if pvs.isOutputting():
                                    pvs.stop()
                                else:
                                    pvs.out()
                                    print('out')
                        else:
                            BASE = midiToHz(math.floor(x*12+b + 50))
                            if not p.isPlaying():
                                p.setArg(([BASE],[0]))
                                #p.play()
                            osc_.setFreq(midiToHz(math.floor(x*12+b + 70)))
                            osc.out()
                            print(b)
                            #the following two lines of code will change the
                            #pitch of the recorded sample:
                            #pvt.setTranspo(pow((13/12.0), round(x) + b-4))
                            #pvs.out()
                            break
        else:
            p.stop()
            osc.stop()
            #pvs.stop()
        #osc.setFreq(midiToHz(math.floor(x*44 + 60)))
    else:
        if joy.get_button(1):
            osc.setFreq(midiToHz(math.floor(x*12 + 70)))
            osc.out()
        elif joy.get_button(2):
            osc.setFreq(midiToHz(math.floor(x*12 + 58)))
            osc.out()
        else:
            osc.stop()

    clk.tick(30)
