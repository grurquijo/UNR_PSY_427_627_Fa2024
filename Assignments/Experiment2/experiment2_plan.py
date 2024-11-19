# Name: Giselle Urquijo
# Date modified: 11/18/2024

import os
import json

from psychopy import gui
from experiment2_functions import *


# use dialogue box to create experiments
    
# you can get dialogue from dict and responses save to a list >>saves as a dict and can be passed into json 
# we're using json just DO IT BITCH
# save plan to json bc it can be opened with other languages and pickle can be big

# use dialogue box to get information about:
#       - use default trial, edit existing, or create new
#           > unique name or generated name
choose_experiment = {'Choose one of the following': ('default experiment', 
                                                     'choose existing experiment', 
                                                     'create new experiment', 
                                                     'edit existing experiment')}

dlg_win_one = gui.DlgFromDict(dictionary=choose_experiment, title='Experiment 2', sortKeys=False, copyDict=True, )

tst = dlg_win_one.dictionary['Choose one of the following']

# im so sad i cant use match case here since its only available in python 3.10 :(
if tst == 'default experiment':
    print('1')
    stimuli_loc = {'Pathname of stimuli folder':'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'}
    dlg_default_experiment = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2', copyDict=True)

    fname = dlg_default_experiment.dictionary
    temp = open_file(filename='./Experiments/default_experiment.json')
    temp["Stimuli location"].append(fname['Pathname of stmuli folder'])
    write_json(data=temp, filename='./Experiments/default_experiment.json')
    
elif tst == 'choose existing experiment':
    print('2')
    saved_trials = {'choose one': []}
    f = list_files(path='./Experiments')
    for i,idx in enumerate(f):
        saved_trials['choose one'].append(f[i])
    
    dlg_choose_existing_experiment = gui.DlgFromDict(dictionary=saved_trials, title='Experiment2', sortKeys=False, copyDict=True)

elif tst == 'create new experiment':
    print('3')
    fname = gen_new_filename()
    #       - name of folder where stimuli exist 
    #           > warn that stimuli should all be in the same folder and uniquely named 
    #           > will search for directory location
    stimuli_loc = {'Pathname of stimuli folder':'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'}

    dlg_win_two = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2',sortKeys=False, copyDict=True)
    #       - for new trial (define what a trial consists of):
    #           > screen size and screen color
    #           > number of trials
    #           > because this is a two alternative forced comparison experiment 
    #               >> what two categories are we comparing/are we comparing just from the same category
    #           > duration of stimulus and max_wait time
    #           
    create_new_trial = {'Screen size (pixels)':'True, False, or [height,width]',
                        'Screen color':'(0.5,0.5,0.5)', 
                        'Number of trials':0, 
                        'Category names':'faces', 
                        'Stimulus duration (s)':0, 
                        'Max wait time (s)':0}

    dlg_win_three = gui.DlgFromDict(dictionary=create_new_trial, title='Experiment 2',sortKeys=False, copyDict=True)

    write_json(data=dlg_win_three.dictionary, filename='./Experiments/'+fname)

elif tst == 'edit existing experiment':
    print('4')
    saved_trials = {'choose one': []}
    f = list_files(path='./Experiments')
    for i,idx in enumerate(f):
        saved_trials['choose one'].append(f[i])
    dlg_edit_existing_experiment = gui.DlgFromDict(dictionary=saved_trials, title='Experiment2', sortKeys=False, copyDict=True)

    chosen_experiment = dlg_edit_existing_experiment.dictionary

    edit_experiment = open_file(filename='./Experiments/' + chosen_experiment['choose one'])

    dlg_edit_existing_experiment = gui.DlgFromDict(dictionary=edit_experiment)