# date modified: 10/3/2024


#%%Imports 
import os
import random
import matplotlib.pyplot as plt
import numpy as np

from psychopy import visual, core
from turtledemo.sorting_animate import instructions1


#%% 
# set-up functions

# take pathname, what to look for in the pathname, and an empty list :)
def find_files(path, opt1, opt2, empty_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(opt1) or file.startswith(opt2):
                empty_list.append(os.path.join(floc_dir, file))
                
# present randomly chosen images from specified list on the left/right side of the little screen :)                
def trial(tnum, array, lr_choice):
    if lr_choice == 'left':
        for i in range(tnum):
            img = visual.ImageStim(win, random.choice(array), pos=(-200,0), size=(300,300), units="pix")
            img2 = visual.ImageStim(win, random.choice(array), pos=(200,0), size=(300,300), units="pix")
            img.draw()
            img2.draw()
            win.flip()
            core.wait(1)

            core.wait(0.25)
        
    elif lr_choice == 'right':
        for i in range(tnum):
            img = visual.ImageStim(win, 
                                   random.choice(array), 
                                   pos=(200,0), 
                                   size=(300,300), 
                                   units="pix")
            img.draw()
            win.flip()
            core.wait(1)

            core.wait(0.25)         

# three second pause between blocks :)
def block_pause():
    message = visual.TextStim(win, text=' ')
    message.autoDraw = True  
    win.flip()
    core.wait(3)



#%%
# set path name and find specified stimuli in floc folder
#curDir = os.path.abspath(os.curdir)
#flocDir = os.path.join(curDir, 'fLoc_stimuli')
#floc_dir = 'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'
floc_dir = 'C:/Users/gis_r/OneDrive/Documents/Python/Assignment 1/fLoc_stimuli'

# note-to-self: there is definitely a better way to do this.
faces = []
find_files(floc_dir, 'adult', 'child', faces)

places = []
find_files(floc_dir, 'house', 'corridor', places)

objects = []
find_files(floc_dir, 'instrument', 'car', objects)



#%%
# Create a small screen window, 
screen_size = [800,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

# start trials
# BLAH
message = visual.TextStim(win, text='Ready?')

message.autoDraw = True  
win.flip()
core.wait(2.0)

message.text = 'Of course you are.'  
win.flip()
core.wait(2.0)

message.text = 'GO'  
win.flip()
core.wait(2.0)

message.text = ' '  
win.flip()
core.wait(.01)

trial(16, faces, 'left')
block_pause()

trial(16, places, 'right')
block_pause()

trial(16, objects, 'left')
block_pause()


win.close()

# %%
