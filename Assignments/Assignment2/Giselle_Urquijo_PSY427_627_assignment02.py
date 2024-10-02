# Name: Giselle Urquijo
# Date modified: 10/1/2024

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
def find_files(path, opt, empty_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(opt):
                empty_list.append(os.path.join(floc_dir, file))
                
# present randomly chosen images from specified list on the left side of the little screen :)                
def trial_left(tnum, array):
    trial = tnum

    for i in range(trial):
        img = visual.ImageStim(win, random.choice(array), pos=(-200,0), size=(300,300), units="pix")
        img.draw()
        win.flip()
        core.wait(1)

        message = visual.TextStim(win, text=' ')
        message.autoDraw = True  
        win.flip()
        core.wait(0.25)
        
# present randomly chosen images from specified list on the right side of the little screen :)          
def trial_right(tnum, array):
    trial = tnum

    for i in range(trial):
        img = visual.ImageStim(win, random.choice(array), pos=(200,0), size=(300,300), units="pix")
        img.draw()
        win.flip()
        core.wait(1)

        message = visual.TextStim(win, text=' ')
        message.autoDraw = True  
        win.flip()
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
floc_dir = 'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'
#floc_dir = 'C:/Users/gis_r/OneDrive/Documents/Python/Assignment 1/fLoc_stimuli'

# note-to-self: there is definitely a better way to do this.
adult = []
find_files(floc_dir, 'adult', adult)

child = []
find_files(floc_dir, 'child', child)

house = []
find_files(floc_dir, 'house', house)

corr = []
find_files(floc_dir, 'corridor', corr)

inst = []
find_files(floc_dir, 'instrument', inst)

car = []
find_files(floc_dir, 'car', car)



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

trial_left(16, adult)
block_pause()

trial_left(16, house)
block_pause()

trial_left(16, inst)
block_pause()

trial_right(16, child)
block_pause()

trial_right(16, corr)
block_pause()

trial_right(16, car)
block_pause()


win.close()

# %%
