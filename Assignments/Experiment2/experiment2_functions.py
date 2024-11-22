# Name: Giselle Urquijo
# Date modified: 11/18/2024

import os
import sys
import json
import psychopy
import numpy as np
import matplotlib.pyplot as plt

from psychopy import visual, core, event
from psychopy.hardware import keyboard
from psychopy.visual.shape import ShapeStim

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

def check_keypress(quit_list:list, key_in, win):#key_response:list, 
    if key_in == 'none':
        print('timed out')
    elif key_in in quit_list:
        print('\033[92m Exiting experiment \033[0m')
        win.saveFrameIntervals()
        win.saveMovieFrames(fileName='./ExperimentMovie.mp4')
        win.close()
        raise
    else: 
        pass
    
    #return key_out, key_time

# (3) Set up the screen.
def screen_setup(screen_size:list, screen_color:any=(0.5,0.5,0.5), fullscreen:bool=False):
    if fullscreen is True:
        win = visual.Window(color=screen_color,
                            fullscr=True,
                            units='pix',
                            )
    else:
        win = visual.Window(size=screen_size,
                            color=screen_color,
                            fullscr=fullscreen,
                            units='pix',) 
    return win
    
def fixation_point(win, fix_color='white'):
    fixation = visual.ShapeStim(win, 
                                vertices=((0, -5), (0, 5), (0,0), (-5,0), (5, 0)),
                                lineWidth=.75,
                                closeShape=False,
                                lineColor=fix_color)
    return fixation

def randomize_matches(size, percent_match):
    '''
    given number of trials(size) assigns a given percentage of True for matching
    size: number of trials
    percent_match: percentage of trials you want to match as a decimal >> 0.25 for 25%
    '''
    match_array = np.random.choice([True,False], size=size, p=[percent_match, 1-percent_match])
    return match_array

def fix_saved_video_frame_rate(key_pressed, win, frame_rate:float=(1/30)):
    _, key_time = key_pressed[0]
    num_rpt = frame_rate * key_time
    num_rpt_rnd = np.round(num_rpt)
    for i in range(int(num_rpt_rnd)):
        win.getMovieFrame()
    return win.getMoveFrame()
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
def trial(repeat:bool, stim:list, stim_duration: float, win, fixation):
    if not repeat:
        img1 = visual.ImageStim(win, stim[0], pos=(-200,0), size=(300,300), units="pix")
        img2 = visual.ImageStim(win, stim[1], pos=(200,0), size=(300,300), units="pix")
    else:
        img1 = visual.ImageStim(win, stim[0], pos=(-200,0), size=(300,300), units="pix")
        img2 = visual.ImageStim(win, stim[0], pos=(200,0), size=(300,300), units="pix")
    
    img1.draw()
    img2.draw()
    
    win.flip()
    x = win.getMovieFrame()
    fixation.draw()
    core.wait(stim_duration)
    win.flip()
    x = win.getMovieFrame()
    # response = event.waitKeys(maxWait=max_wait,
    #                                       timeStamped=True, 
    #                                       clearEvents=True,), max_wait
    
    return x
# You should write your code to be flexible enough to quickly implement a change in image directory (to show other same/different images). That will be your next assignment!