import os
import json
import psychopy
import numpy as np

from psychopy import visual, core, event
from experiment2_functions import *


############################ SET UP BEGINS HERE ############################ 

# load experiment
load_exp = open_file(filename='./load_experiment.json')
exp_info = open_file(filename=load_exp['Experiment to load'])
exp_set_up = exp_info['Experiment set-up']
print('Experiment loaded')


# need to change screen color list to tuple
screen_color_str = exp_set_up['Screen color'].split(',')
screen_color_list = [float(i) for i in screen_color_str]


# Set up all the variables
stim_location = exp_info['Stimuli location']
fullscreen = eval(exp_set_up["Full screen"])
screen_size = exp_set_up["Screen size (pixels)"].split(',')
screen_color = tuple(screen_color_list)
stim_categories = exp_set_up['Category names'].split(',')
stim_duration = exp_set_up['Stimulus duration (s)']
trial_num = exp_set_up['Number of trials']
max_wait = exp_set_up['Max wait time (s)']
print('Variables set')

# Grabbing stimuli for experiment
exp_stim = []
find_files(path=stim_location, empty_list=exp_stim, file_name=stim_categories)
print('Stimuli collected')


# Set up window for experiment
win = screen_setup(screen_size=screen_size, fullscreen=fullscreen, screen_color=screen_color)


# Experiment description and instructions
exp2_message = visual.TextStim(win, text='In this experiment, you will be comparing two images side by side and determining if they are the same or different.'
                '\n'
                '\n During any point in the experiment press "esc" or "Q" to quit.'
                '\n\nPress any key to continue.')
exp2_message.draw()
win.flip()
event.waitKeys()

# Grabbing preferred response key
keys_equal = True
key_response = []
key_quit = ['escape', 'q']

while keys_equal:
    message = visual.TextStim(win, text='Please choose a response key for "same" that isn\'t "q" or "esc".')

    message.setAutoDraw(False)
    message.draw()
    win.flip()
    key_same = event.waitKeys(clearEvents=True)

    message.setText('Choose a response key for "different".') 
    message.draw()
    win.flip()
    key_different = event.waitKeys(clearEvents=True)


    if key_same[0] and key_different[0] in key_quit:
        print('here')
        win.flip()
        pass
    elif key_same == key_different:
        print('no here')
        win.flip()
        pass
    else:
        win.flip()
        keys_equal = False

############################ TRIAL BEGINS HERE ############################ 
# for i in trial_num:
#     participant_response = trial(stim=exp_stim, stim_duration=stim_duration, win=win)
#     check_keypress(key_list=[key_response, key_quit], key_in=participant_response)


win.close()
core.quit()