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
choose_experiment = {'Choose one of the following': ('',
                                                     'default experiment', 
                                                     'choose existing experiment', 
                                                     'create new experiment', 
                                                     'edit existing experiment')}

dlg_win_one = gui.DlgFromDict(dictionary=choose_experiment, title='Experiment 2', sortKeys=False, copyDict=True, )

tst = dlg_win_one.dictionary['Choose one of the following']

# im so sad i cant use match case here since its only available in python 3.10 :(
if tst == 'default experiment':
    print('1')
    load_experiment = open_file(filename='./load_experiment.json')
    load_experiment.update({'Experiment to load': './Experiments/default_experiment.json'})
    write_json(data=load_experiment, filename='./load_experiment.json')
    
    stimuli_loc = {'Pathname of stimuli folder':'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'}
    dlg_default_experiment = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2', copyDict=True)

    fname = dlg_default_experiment.dictionary['Pathname of stimuli folder']
    
    temp = open_file(filename='./Experiments/default_experiment.json')
    temp.update({'Stimuli location': fname})
    
    write_json(data=temp, filename='./Experiments/default_experiment.json')
    
elif tst == 'choose existing experiment':
    print('2')
    
    saved_trials = {'choose one': []}
    f = list_files(path='./Experiments')
    for i,idx in enumerate(f):
        saved_trials['choose one'].append(f[i])
    
    dlg_choose_existing_experiment = gui.DlgFromDict(dictionary=saved_trials, title='Experiment2', sortKeys=False, copyDict=True)
    
    stimuli_loc = {'Pathname of stimuli folder':''}
    dlg_stim_loc = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2', copyDict=True)

    fname = dlg_stim_loc.dictionary['Pathname of stimuli folder']
    
    temp = open_file(filename='./Experiments/'+dlg_choose_existing_experiment.dictionary['choose one'])
    temp.update({'Stimuli location': fname})
    
    write_json(data=temp, filename='./Experiments/'+dlg_choose_existing_experiment.dictionary['choose one'])
    
    
    load_experiment = open_file(filename='./load_experiment.json')
    load_experiment.update({'Experiment to load': './Experiments/'+dlg_choose_existing_experiment.dictionary['choose one']})
    
    write_json(data=load_experiment, filename='./load_experiment.json')
    

elif tst == 'create new experiment':
    print('3')
    fname = gen_new_filename()
    
    load_experiment = open_file(filename='./load_experiment.json')
    load_experiment.update({'Experiment to load': './Experiments/'+fname})
    write_json(data=load_experiment, filename='./load_experiment.json')
    #       - name of folder where stimuli exist 
    #           > warn that stimuli should all be in the same folder and uniquely named 
    #           > will search for directory location
    stimuli_loc = {'Pathname of stimuli folder':'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'}

    dlg_stim_loc = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2',sortKeys=False, copyDict=True)
    #       - for new trial (define what a trial consists of):
    #           > screen size and screen color
    #           > number of trials
    #           > because this is a two alternative forced comparison experiment 
    #               >> what two categories are we comparing/are we comparing just from the same category
    #           > duration of stimulus and max_wait time
    #           
    create_new_trial = {'Full screen': ['True', 'False'],
                        'Screen size (pixels)':'height,width',
                        'Screen color':'0.5,0.5,0.5', 
                        'Number of trials':0, 
                        'Category names':'option 1, option 2', 
                        'Stimulus duration (s)':0, 
                        'Max wait time (s)':0}
    
    template = {'Stimuli location': dlg_stim_loc.dictionary['Pathname of stimuli folder'], 'Experiment set-up': {}}
    write_json(data=template, filename='./Experiments/'+fname)
    
    dlg_create_new_experiment = gui.DlgFromDict(dictionary=create_new_trial, title='Experiment 2',sortKeys=False, copyDict=True)
    
    template["Experiment set-up"].update(dlg_create_new_experiment.dictionary)

    write_json(data=template, filename='./Experiments/'+fname)

elif tst == 'edit existing experiment':
    print('4')
    saved_trials = {'choose one': []}
    f = list_files(path='./Experiments')
    for i,idx in enumerate(f):
        saved_trials['choose one'].append(f[i])
    dlg_choose_existing_experiment = gui.DlgFromDict(dictionary=saved_trials, title='Experiment2', sortKeys=False, copyDict=True)
    
    stimuli_loc = {'Pathname of stimuli folder':''}
    dlg_stim_loc = gui.DlgFromDict(dictionary=stimuli_loc, title='Experiment 2', copyDict=True)
    
    chosen_experiment = dlg_choose_existing_experiment.dictionary['choose one']
    edit_experiment = open_file(filename='./Experiments/' + chosen_experiment)

    dlg_edit_existing_experiment = gui.DlgFromDict(dictionary=edit_experiment['Experiment set-up'], title='Experiment 2',sortKeys=False, copyDict=True)
    
    temp = open_file(filename='./Experiments/'+dlg_choose_existing_experiment.dictionary['choose one'])
    temp.update({'Stimuli location': dlg_stim_loc.dictionary['Pathname of stimuli folder'], 'Experiment set-up': edit_experiment['Experiment set-up']})
    
    write_json(data=temp, filename='./Experiments/'+dlg_edit_existing_experiment.dictionary['choose one'])
    