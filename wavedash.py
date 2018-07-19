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

t = NewTable(length = 6, chnls = 1)
a = Input(0)
#amp = Iter(T['trig'], [10])
#https://groups.google.com/forum/#!topic/pyo-discuss/YO-qhUq-ApE

#Freq = t.getRate()

#pva = PVAnal(c, size=1024)
#pvt = PVTranspose(pva, transpo=1)#changing value of transpo can pitch shift
#pvs = PVSynth(pvt)

#c = Osc(t, [Freq], mul=1).out()

#p = Pattern(pat, .2, ([0],[0]))


#def pat():
#    print('hello')
    
#yungmetro.play()


class MonolithPleaseChangeNameLater:
    
    def __init__(self):
        pass
        #self.recording = False
        self.dirtyslots = [NewTable(length = 6, chnls = 1) for i in range(4)]
        self.recorders = [TableRec(a, self.dirtyslots[i], 0.0) for i in range(4)]
        self.loopers = [Looper(self.dirtyslots[i],1,dur=4,mul=1.7, startfromloop=False) for i in range(4)]
        for l in self.loopers:
            l.appendFadeTime(True)
        self.BPM = 120
        self.beatspermeasure = 4

    def pat_print_metronome(self, arg):
        if arg[0] < self.beatspermeasure-1:
            print("--{}--".format(arg[0]+1))
        elif arg[0] == self.beatspermeasure-1:
            print("--{}!!!".format(arg[0]+1))
        else:
            #print("{:.2f}".format(self.T['time'].get()/33000))
            print(1+(arg[0]%self.beatspermeasure))
        arg[0]+=1
    
    def process_button(self, button):
        if button in [0,1,2,3]:
            #if not self.recording:
            if joy.get_button(5):
                print("recordingis starting")
                #self.recording = True
                
                self.yungmetro = Pattern(self.pat_print_metronome, arg = [[0]], time=60.0/self.BPM)
                
                self.yungmetro.play(3*self.beatspermeasure*60.0/self.BPM)
                self.xasd = CallAfter(self.recorders[button].play, time=self.beatspermeasure*60.0/self.BPM)
                #self.T.play()
                
                
                
            else:
                #print(self.T['trig'])
                if self.loopers[button].isOutputting():
                    self.loopers[button].stop()
                    print("{} stop".format(button))
                else:
                    
                    self.loopers[button].reset()#this line makes the loop play from the beginning when u stop and start it.
                    self.loopers[button].out()
                    print('{} play'.format(button))

    def go(self):
        """maybe come up with a better name for this too?
        man I'm bad at programming xD"""
        while True:
        #tix+=1
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    import sys
                    sys.exit()
                elif event.type == pygame.JOYBUTTONDOWN:
                    self.process_button(event.button)

            x = joy.get_axis(0)
            y = joy.get_axis(1)
            x2 = joy.get_axis(3)
            y2 = joy.get_axis(2)
            l = joy.get_axis(4)
            r = joy.get_axis(5)
            for b in range(joy.get_numbuttons()):
                    
                        #else:
                            #recording = False
                            
                if joy.get_button(b):
                            if b in [2,5]:
                                pass
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
        ##    else:
        ##        if joy.get_button(1):
        ##            osc.setFreq(midiToHz(math.floor(x*12 + 70)))
        ##            osc.out()
        ##        elif joy.get_button(2):
        ##            osc.setFreq(midiToHz(math.floor(x*12 + 58)))
        ##            osc.out()
        ##        else:
        ##            pass#osc.stop()

            clk.tick(30)
m = MonolithPleaseChangeNameLater()
m.go()
