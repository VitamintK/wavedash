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
osc = LFO(freq=freq,mul=0.9)

b = Degrade(osc, bitdepth=8).out()
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

#create display
#size = width, height = 600, 600
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("game game game")

#frame xhair zone
#frameRect = pygame.Rect((45,45), (510,510))

#generate crosshair
#crosshair = pygame.surface.Surface((10,10))
#crosshair.fill(pygame.Color("magenta"))
#pygame.draw.circle(crosshair,pygame.Color("grey"), (5,5), 5, 0)
#crosshair.set_colorkey(pygame.Color("magenta"), pygame.RLEACCEL)
#crosshair = crosshair.convert()
# Generate crosshair 2
#crosshair2 = pygame.surface.Surface((10, 10))
#crosshair2.fill(pygame.Color("magenta"))
#pygame.draw.circle(crosshair2, pygame.Color("yellow"), (5,5), 5, 0)
#crosshair2.set_colorkey(pygame.Color("magenta"), pygame.RLEACCEL)
#crosshair2 = crosshair2.convert()
# Generate crosshair L/R
#crosshairtrigger = pygame.surface.Surface((10, 10))
##crosshairtrigger.fill(pygame.Color("magenta"))
#pygame.draw.circle(crosshairtrigger, pygame.Color("red"), (5,5), 5, 0)
#crosshairtrigger.set_colorkey(pygame.Color("magenta"), pygame.RLEACCEL)
#crosshairtrigger = crosshairtrigger.convert()
# Generate pepperoni
#pep = pygame.surface.Surface((100, 100))
#pep.fill(pygame.Color("magenta"))
#pygame.draw.circle(pep, pygame.Color("pink"), (50,50), 50, 0)
#pep.set_colorkey(pygame.Color("magenta"), pygame.RLEACCEL)
#pep = pep.convert()


#randloc = (random.random()*200+100, random.random()*200 + 100)

ARPEGGIO = [0,3,6]
osc.stop()
import math
#tix = 0

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
    #print(joy.get_axis(2))
    x2 = joy.get_axis(3)
    y2 = joy.get_axis(2)
    l = joy.get_axis(4)
    r = joy.get_axis(5)
    #if(tix%600 == 0):
    #    randloc = (random.random()*200+100, random.random()*200 + 100)
    #screen.fill(pygame.Color('black'))
    #screen.blit(pep, randloc)
    #screen.blit(crosshair, ((x*250)+300-5, (y*250)+300-5))
    #screen.blit(crosshair2, ((x2*250)+300-5, (y2*250)+300-5))
    #screen.blit(crosshairtrigger, ((l*250)+300-5, (r*250)+300-5))
    #pygame.display.flip()
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
                                pass#recording 
                        else:
                            #osc.setFreq(midiToHz(math.floor(x*12+b + 70)))
                            #osc.out()
                            print(b)
                            #c.setPitch(b/14.0+.85)
                            #c.out()
                            pvt.setTranspo(b/12.0 + .12)
                            break
        else:
       		osc.stop()
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
