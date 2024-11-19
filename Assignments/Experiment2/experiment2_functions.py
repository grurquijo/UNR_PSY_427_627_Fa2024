# Name: Giselle Urquijo
# Date modified: 11/18/2024

import os
import sys
import json
import psychopy
import matplotlib.pyplot as plt

from psychopy import visual, core, event
from psychopy.hardware import keyboard


# Json file management
def write_json(data, filename:str):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def open_file(filename:str):
    with open(filename) as f:
        load_file = json.load(f)

    return load_file

def does_file_exist(filename:str):
    dir_list = os.listdir('./Experiments/')
    for f in dir_list:
        if f == filename:
            return True
    
    return False

def gen_new_filename():
    if not does_file_exist("Experiment0.json"):
        return "Experiment0.json"
    else:
        for i in range(100):
            i += 1
            if not does_file_exist('Experiment' + str(i) + '.json'):
                return 'Experiment' + str(i) + '.json'
            
    return False


def list_files(path:str) -> list:
    '''
    Finds and appends all files in a specified directory to a list and returns it.
    '''
    file_list = []
    dir_list = os.listdir(path)
    dir_string = ""
    print("--- List of files ---")
    for f in dir_list:
        dir_string += f + " "
        file_list.append(f)
        print('\033[92m' + f + '\033[0m')
    print("--- End of list ---")

    return file_list

# (1) Get all images that match a certain pattern (i.e. contain some sub-string) from a directory. The directory and sub-string should be the inputs, and a list or cell array of file names should be the output

def find_files(path:str, empty_list:list, file_name:list) -> list:
    '''
    Look for given files in a path. Returns list off all files found.
    '''
    for x in file_name:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.startswith(x):
                    empty_list.append(os.path.join(path, file))
    
    return empty_list

# (2) Collect responses

def check_keypress(key_list:list, key_in):
    if key_in[0] == key_list[0]:
        key_out, key_time = key_in
        print(key_out)
    elif key_in[0] == key_list[1]:
        raise Exception ('Quit Experiment')
    
    return key_out, key_time

# (3) Set up the screen.
def screen_setup(screen_size:list, screen_color:any=(0.5,0.5,0.5), fullscreen:bool=False):
    if fullscreen is True:
        win = visual.Window(color=screen_color,
                            fullscr=True,
                            units='pix',)
    else:
        win = visual.Window(size=screen_size,
                            color=screen_color,
                            fullscr=fullscreen,
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
def trial(trial_num:int, stim_list:list, stim_duration: float, win):
    while trial_num >= 0:
        img1 = visual.ImageStim(win, stim_list, pos=(-200,0), size=(300,300), units="pix")
        img2 = visual.ImageStim(win, stim_list, pos=(200,0), size=(300,300), units="pix")
        img1.draw()
        img2.draw()
        win.flip()
        core.wait(stim_duration)
        trial_num -=1
# You should write your code to be flexible enough to quickly implement a change in image directory (to show other same/different images). That will be your next assignment!