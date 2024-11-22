# Name: Giselle Urquijo
# Date modified: 11/19/2024

import os
import json
import datetime
import psychopy
import numpy as np

from moviepy.editor import *

from psychopy import visual, core, event
from experiment2_functions import *


############################ SET UP BEGINS HERE ############################ 

# grabbing date and time for logging

exp_time = datetime.datetime.now()
mon_day_yr = exp_time.strftime("%m/%d/%Y")

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
stim_duration = float(exp_set_up['Stimulus duration (s)'])
trial_num = exp_set_up['Number of trials']
match_num = exp_set_up['Number of matches'] / trial_num
max_wait = float(exp_set_up['Max wait time (s)'])
print('Variables set')

match_array = randomize_matches(size=trial_num, percent_match=match_num)

# Grabbing stimuli for experiment
exp_stim = []
find_files(path=stim_location, empty_list=exp_stim, file_name=stim_categories)
print('Stimuli collected')


# Set up window for experiment, set quit keys, and begin checking for quit key press
key_quit = ['escape', 'q']
win = screen_setup(screen_size=screen_size, fullscreen=fullscreen, screen_color=screen_color)
win.recordFrameIntervals = True
framerate = win.monitorFramePeriod

# Experiment description and instructions
exp2_message = visual.TextStim(win, text='In this experiment, you will be comparing two images side by side and determining if they are the same or different.'
                '\n'
                '\n During any point in the experiment press "esc" or "Q" to quit.'
                '\n\nPress any key to continue.')
exp2_message.draw()
win.flip()
win.getMovieFrame()
key_pressed= event.waitKeys(clearEvents=True, timeStamped=True)
check_keypress(quit_list=key_quit, key_in=key_pressed, win=win)
# _, key_time = key_pressed[0]
# num_rpt = (1/30) * key_time
# num_rpt_rnd = np.round(num_rpt)
# for i in range(int(num_rpt_rnd)):
#     win.getMovieFrame()

#y_me = fix_saved_video_frame_rate(key_pressed=key_pressed, win=win)


# Grabbing preferred response key
keys_equal = True

fixation_neutral = fixation_point(win=win, fix_color='white')
fixation_correct = fixation_point(win=win, fix_color='lime')
fixation_incorrect = fixation_point(win=win,fix_color='red')

while keys_equal:
    participant_keys = []
    message = visual.TextStim(win, text='Please choose a response keys for that aren\'t "q" or "esc".'
                              '\n'
                              '\n\nPress any key to continue or "esc"/"Q" to quit.')
    
    message.setAutoDraw(False)
    message.draw()
    win.flip()
    win.getMovieFrame()
    key_pressed = event.waitKeys(clearEvents=True)
    check_keypress(quit_list=key_quit, key_in=key_pressed[0], win=win)
    
    message.setText('Choose a response key for "same".')
    message.draw()
    win.flip()
    win.getMovieFrame()
    key_same = event.waitKeys(clearEvents=True)
    participant_keys.append(key_same[0])
    check_keypress(quit_list=key_quit, key_in=key_same[0], win=win)#key_response=[],

    message.setText('Choose a response key for "different".')
    message.draw()
    win.flip()
    win.getMovieFrame()
    key_different = event.waitKeys(clearEvents=True)
    participant_keys.append(key_different[0])
    check_keypress(quit_list=key_quit, key_in=key_different[0], win=win)#key_response=[]


    # if key_same[0] and key_different[0] in key_quit:
    #     message.setText('Your response keys must be different. Press any key to continue.') 
    #     print('response = quit')
    #     win.flip()
    #     key_pressed = event.waitKeys(clearEvents=True)
    #     check_keypress(key_list=key_quit, key_in=key_pressed, win=win)
    #     pass
    # el
    if key_same == key_different:
        message.setText('Your response keys must be different. Press any key to continue.') 
        message.draw()
        print('response = response')
        win.flip()
        win.getMovieFrame()
        key_pressed = event.waitKeys(clearEvents=True)
        check_keypress(quit_list=key_quit, key_in=key_pressed, win=win)
        pass
    else:
        print('Response keys set')
        win.flip()
        win.getMovieFrame()
        keys_equal = False

# open up txt file to log responses(correct/incorrect), and responses
fid = open("./Logs/data.txt", "a")
fid.write('\n\n'+mon_day_yr+
          '\nData for ' + load_exp['Experiment to load']+':')



############################ TRIAL BEGINS HERE ############################ 
clock_init = core.Clock()
for i in range(trial_num):
    fixation_neutral.draw()
    
    img_repeat = match_array[i]
    next_stim = [i for i in np.random.choice(exp_stim, size=2, replace=False)]
    
    tmp = trial(repeat=img_repeat,stim=next_stim, stim_duration=stim_duration, win=win, fixation=fixation_neutral)#, max_wait=max_wait
    t0 = clock_init.getTime()
    response = event.waitKeys(maxWait=max_wait,
                                          timeStamped=clock_init, 
                                          clearEvents=True,)
    
    try:
        key, time = response[0]
    except TypeError:
        key = 'Timed out'
        time = max_wait
        pass
    
    delta_time = time - t0
    print(key, delta_time)

    x = check_keypress(win=win,
                       quit_list=key_quit,
                       key_in=key)
    
    if (key == participant_keys[0]) and (img_repeat == True):
        fid.write('\nKey: '+key+
                  '\nResponse Time: '+str(delta_time)+
                  '\nCorrect: Yes \n')
        fixation_correct.draw()
        win.flip()
        key_pressed = event.getKeys()
        if key_pressed is not None:
            check_keypress(win=win,
                        quit_list=key_quit,
                        key_in=key_pressed)
        win.getMovieFrame()
        core.wait(1)
    elif (key == participant_keys[1]) and (img_repeat == False):
        fid.write('\nKey: '+key+
                  '\nResponse Time: '+str(delta_time)+
                  '\nCorrect: Yes\n')
        fixation_correct.draw()
        win.flip()
        key_pressed = event.getKeys()
        if key_pressed is not None:
            check_keypress(win=win,
                        quit_list=key_quit,
                        key_in=key_pressed)
        win.getMovieFrame()
        core.wait(1)
    else:
        fid.write('\n Key: '+key+
                  '\nResponse Time: '+str(delta_time)+
                  '\nCorrect: No\n')
        fixation_incorrect.draw()
        win.flip()
        key_pressed = event.getKeys()
        if key_pressed is not None:
            check_keypress(win=win,
                        quit_list=key_quit,
                        key_in=key_pressed)
        win.getMovieFrame()
        core.wait(1)
win.flip()
frame_times = [i for i in win.frameIntervals]
frame_images = [np.array(i) for i in win.movieFrames]
images_array = []
for i,idx in enumerate(frame_images):
    print(i, idx)
    
    images_array.append(np.array(idx))
frame_tuples = list(zip(images_array, frame_times))
# test = VideoClip(make_frame, duration=)
# final_clip = concatenate_videoclips(exp_clips)
# final_clip.write_videofile('./testing.mp4', fps=30)
#exp_clips = np.array(exp_clips)
clip = ImageSequenceClip(np.array(frame_tuples), fps=30)
clip.write_videofile('./anothertest.mp4')
print(str(len(win.movieFrames)))
print(str(len(win.frameIntervals)))
#look at ImageClip.setduration
win.saveFrameIntervals(fileName='./experimentframetest.json')
win.saveMovieFrames(fileName='./ExperimentMovie.mp4')
fid.close()    
win.close()
core.quit()