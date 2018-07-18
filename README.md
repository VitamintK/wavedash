# wavedash
The GameCube controller is a musical instrument

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

