#%%
# Imports
import os
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from functions import *



floc_dir = 'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'
#floc_dir = 'C:/Users/gis_r/Documents/Python/Assignment 1/fLoc_stimuli'

fullscr = [800,800] #True
max_wait = .5
win = visual.Window(color=(0.5,0.5,0.5),
                    fullscr=fullscr,
                    units='pix',)


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
        keys_equal = False


# grab stimuli
faces = []
find_files(floc_dir, 'adult', 'child', faces)

faces_trial = [i for i in np.random.choice(faces, size=40)]

places = []
find_files(floc_dir, 'house', 'corridor', places)

places_trial = [i for i in np.random.choice(places, size=40)]

objects = []
find_files(floc_dir, 'instrument', 'car', objects)

objects_trial = [i for i in np.random.choice(objects, size=40)]

shuffle = np.hstack((faces_trial, places_trial, objects_trial))

shuffle_trial = [i for i in np.random.choice(shuffle, size=40)]



trial_order = [faces_trial,faces_trial,
               places_trial,places_trial,
               objects_trial,objects_trial,
               shuffle_trial,shuffle_trial]

np.random.shuffle(trial_order)


fid = open("./Data_Collected/experiment1_data.txt", "a")

for i,idx in enumerate (trial_order):
    
    trial_message = visual.TextStim(win, text='Block '+ str(i+1))
    trial_message.draw()
    win.flip()
    check_keypress(max_wait=2, key_q=key_quit, f=fid, win=win)
    core.wait(2)
    
    message.setText('Reminder: As you watch the images go by, please press your chosen response button as fast as you can if you see a repeated image.') 
    message.draw()
    win.flip()
    check_keypress(max_wait=4, key_q=key_quit, f=fid, win=win)
    core.wait(4.0)
    
    trial(win, i, 20, idx, key_response, key_quit, fid, max_wait)
    
    win.flip()
    core.wait(2)

fid.close()
win.close()
core.quit()


