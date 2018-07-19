# wavedash
The GameCube controller is a musical instrument

Currently in version -0.1 (negative 0.1)

Requirements:  
GameCube controller (to use as a musical instrument)  
USB GameCube adapter (to connect controller to computer)  
the python script in this repository  
pyo (installation instructions at https://github.com/belangeo/pyo )  
pygame (can be installed with pip)

Then I run on mac using

>python wavedash.py

or on windows by

>python wavedash.py asio



For the little snippets in the pyo-examples/ directory, I have to run most of them (that aren't in an infinite loop) with 

> python -i snippet.py

because I think I didn't install all the GUI stuff on windows, so the program otherwise instantly ends and quits.



The meat of this project is using pyo as an audio engine.  Shoutouts to pyo.



#### How to use

I'm not really sure yet what wAvedAsh actually is.  
I vacillated between it being a sampler/looper (seems kind of lame) and an instrument.  It started off as an instrument.  The prototype was that each button was a note in the 12-tone western music system, and the control stick left and right modulates (either quantized to notes on the 12 tone scale or not - it currently quantizes, and I had an idea to let the c-stick modulate more finely, without quantization.  Also for the vertical axis on the control stick to control volume).  But it was not enough.

So, as it currently stands in this repository (as of 2018/07/18), the A, B, X, and Y buttons have looping functionality, and the recording is using your microphone.

Each of the 4 buttons corresponds to its own loop slot.  If you press one of the buttons while holding R, waVedash will begin recording in that slot (after a countdown).  (Currently each slot has duration of 4 seconds; obviously this should be configurable in the future or maybe you can add it and send a pull request :) or you can just change it to whatever amount you want locally).  Then, to start/stop playback, just press that button again while not holding R.  

When the recording button combination is pressed, the recording will begin after a countdown in stdout.  The counts in stdout will continue into the recording period.  Currently, the count is hardcoded as 4 counts before recording starts, then 8 counts during recording. (so, it's 4/4 time with 1 measure before recording, and 2 measures of recording.)  I'm pretty sure the counting will break if you try to record multiple slots at once. 

This is still version -0.1 (negative 0.1) so I'm not sure what happens if you try to play back while recording.  I think it'll just start playing back from the start and recording at the same time, so you can do that if you want.

It's pretty lame that you have to wait for a countdown before recording, since it impedes the liveness of the looping creation process.  But it's necessary, since I often want to use my hands to play the instrument that I'm recording, and if the recording starts instantaneously, I won't get to play that initial note.  That's the downside of having the looper controlled by your hands and not your feet, as is more usual, I guess.  Plus, since it's a predetermined loop count, the program must determine the beats, and the human must follow - whereas if you could control the looper with your feet, you could determine the beats and start and stop the measure accordingly.

Oh, and the other unmentioned buttons still play a sine-wave kind of sound that can be modulated with the control stick for now.

Anyways, this is fully usable now, so I wrote up this shitty stream-of-consciousness/documentation, if anyone happens upon this and wants to check it out.  It's pretty fun and practical, and pyo and pygame are easy to install, so give it a shot with your instrument/voice/banging on furniture/household objects!