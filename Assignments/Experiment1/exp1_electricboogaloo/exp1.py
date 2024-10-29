import os
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from functions import *
# setup experiment
experiment_load
# create window
fullscr = [800,800] #True
max_wait = .5
win = visual.Window(color=(0.5,0.5,0.5),
                    fullscr=fullscr,
                    units='pix',)

# ask for continue and quit buttons
keys_equal = True

while keys_equal:
    message = visual.TextStim(win, text='Please choose one key for your responses and a different key to quit the experiment at any time.')

    message.setAutoDraw(False)
    message.draw()
    win.flip()
    event.waitKeys(clearEvents=True)

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
        keys_equal = False
        
# show instructions
check_keypress
exp1_message = visual.TextStim(win, text='In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images.'
                '\n\nAs you watch the images go by, please press ' + key_response +' as fast as you can if you see a repeated image.'
                '\n\n Press ' + key_response + ' to continue.')
exp1_message.draw()
win.flip()
#       check for keypress
# grab experiment starting time
exp_t0 = core.Clock()
# begin block
try:
    for i in block_num:
        for j in trial_num:
            check_keypress
#       laod image/fixation
            load_image
            load_fix
#       show image/fixation
            img.draw
            fix.draw
            win.flip()
#       grab time
            exp_t1 = core.Clock()
#       check for keypress
#           if quit key >> exit out
#           if response key 
#               log keypress time
#               repeated image?
#                   if yes 
#                       check keypress for quit
#                       fixation green for 2 seconds
#                       log image time since beginning of experiment
#                       log keypress response time
#                    if not
#                       check keypress for quit
#                       fixation red for 2 seconds
#                       log keypress response time
#
except:
    win.close()
    # Raise last error
    raise