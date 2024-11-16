import os
import sys
import psychopy
import matplotlib.pyplot as plt

from psychopy import visual, core, event
from psychopy.hardware import keyboard

# (1) Get all images that match a certain pattern (i.e. contain some sub-string) from a directory. The directory and sub-string should be the inputs, and a list or cell array of file names should be the output

def find_files(path:str, empty_list:list, key_words:list):
    for x in key_words:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.startswith(x):
                    empty_list.append(os.path.join(path, file))    

# (2) Collect responses

def check_keypress(key_list:list, key_in):
    if key_in == key_list[0]:
        key_out, key_time = event.waitKeys()
    elif key_in == key_list[1]:
        raise Exception ('Quit Experiment')
    return key_out, key_time

# (3) Set up the screen.
def screen_setup(screen_size:list, fullscreen:False, screen_color:list|'gray'):
    if fullscreen is True:
        win = visual.Window(color=screen_color,
                            fullscr=True,
                            units='pix',)
    else:
        win = visual.Window(color=(0.5,0.5,0.5),
                    fullscr=screen_size,
                    units='pix',) 
    return win
    
 
# Inputs should be:

# screen size

# a boolean (True/False) variable for fullscreen or not that defaults to NOT fullscreen

# screen color

# the function should return:

# the screen window object or handle (win, in most of the example code you have).

# You should have a separate function to make a trial plan for all (n) trials.
# Start with the fLoc images (for your next assignment, you will use a differenet set of images). 
# Choose pairs to be members of the same sub-class (e.g. an adult faces and another adult face) 
# or from different categories (e.g. an adult face and a car). Half the presented images should be the same, 
# and half should be different.

# Images should be displayed for 100 ms, exactly.

# The experiment should contain 30 trials.
# what exactly is in a trial? is one trial just one judgement or are we doing categories as trials??
def trial(trial_num:int, stim_list:list, stim_duration:float, win=win):
    while trial_num >= 0:
        img1 = visual.ImageStim(win, random.choice(stim_list), pos=(-200,0), size=(300,300), units="pix")
        img2 = visual.ImageStim(win, random.choice(array), pos=(200,0), size=(300,300), units="pix")
        img1.draw()
        img2.draw()
        win.flip()
        core.wait(stim_duration)
        trial_num -=1
# You should write your code to be flexible enough to quickly implement a change in image directory (to show other same/different images). That will be your next assignment!