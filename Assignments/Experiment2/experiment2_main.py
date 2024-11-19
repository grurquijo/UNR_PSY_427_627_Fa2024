import os
import json
import psychopy
import numpy as np

from psychopy import visual, core, event
from experiment2_functions import *

# load experiment

load_exp = open_file(filename='./load_experiment.json')
exp_info = open_file(filename=load_exp['Experiment to load'])
exp_set_up = exp_info['Experiment set-up']
print('yes')


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

print('yes')

# Grabbing stimuli for experiment
exp_stim = []
find_files(path=stim_location, empty_list=exp_stim, file_name=stim_categories)

win = screen_setup(screen_size=screen_size, fullscreen=fullscreen, screen_color=screen_color)


# Experiment description and instructions
exp2_message = visual.TextStim(win, text='In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images.'
                '\nAs you watch the images go by, please press your chosen response button as fast as you can if you see a repeated image.'
                '\n During any point in the experiment press "esc" or "Q" to quit.'
                '\n\nPress any key to continue.')
exp2_message.draw()
win.flip()
event.waitKeys()

# Grabbing preferred response key
keys_equal = True
key_quit = ['escape', 'q']
while keys_equal:
    message = visual.TextStim(win, text='Please choose a response key that isn\'t "q" or "esc".')

    message.setAutoDraw(False)
    message.draw()
    win.flip()
    key_response = event.waitKeys(clearEvents=True)
    
    if key_response[0] in key_quit:
        win.flip()
        pass
        
    else:
        win.flip()
        keys_equal = False

print(key_response)   
win.close()
core.quit()