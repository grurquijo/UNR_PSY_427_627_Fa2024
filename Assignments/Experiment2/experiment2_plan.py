import os
import json

from psychopy import gui
# use dialogue box to create experiments
    
# you can get dialogue from dict and responses save to a list
# json writer and parser DO IT BITCH THIS IS THE PLACE TO DO IT
# save plan to json bc it can be opened with other languages and pickle can be big

# use dialogue box to get information about:
#       - use default trial, edit existing, or create new
#           > unique name or generated name
choose_trial = {'Choose one of the following': ('default trial', 'choose existing trial', 'create new trial', 'edit existing trial')}

dlg_win_one = gui.DlgFromDict(dictionary=choose_trial, title='Experiment 2', sortKeys=False)
#       - name of folder where stimuli exist 
#           > warn that stimuli should all be in the same folder and uniquely named 
#           > will search for directory location
stimuli_loc = {'Name of folder(s) where stimuli is located':'floc_stimuli'}

dlg_win_two = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2',sortKeys=False)
#       - for new trial (define what a trial consists of):
#           > screen size and screen color
#           > number of trials
#           > because this is a two alternative forced comparison experiment 
#               >> what two categories are we comparing/are we comparing just from the same category
#           > duration of stimulus and max_wait time
#           
create_new_trial = {'Screen size':'True, False, or [300,300]',
                    'Screen color':'[0.5,0.5,0.5]', 
                    'Number of trials':0, 
                    'Category names':'faces', 
                    'Stimulus duration (s)':0, 
                    'Max wait time (s)':0}

dlg_win_three = gui.DlgFromDict(dictionary=create_new_trial, title='Experiment 2',sortKeys=False, copyDict=True)

print(dlg_win_three.dictionary)