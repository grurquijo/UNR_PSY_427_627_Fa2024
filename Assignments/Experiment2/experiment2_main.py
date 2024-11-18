import os
import json
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from experiment2_functions import *


exp1_message = visual.TextStim(win, text='In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images.'
                '\n\nAs you watch the images go by, please press your chosen response button as fast as you can if you see a repeated image.')
exp1_message.draw()
win.flip()
core.wait(10)


keys_equal = True

while keys_equal:
    message = visual.TextStim(win, text='Please choose one key for your responses and a different key to quit the experiment at any time.')

    message.setAutoDraw(False)
    message.draw()
    win.flip()
    core.wait(4.0)

    message.setText('Choose a response key.') 
    message.draw()
    win.flip()
    key_response = event.waitKeys(clearEvents=True) 

    message.setText('Choose a quit key.' )
    message.draw()   
    win.flip()
    key_quit = event.waitKeys(clearEvents=True) 
    
    if key_response == key_quit:
        win.flip()
        pass
    else:
        win.flip()
        keys_equal = 'hello'