# Name: Giselle Urquijo
# Date Modified: 10/10/2024

'''
Please upload a script that computes reaction time from the onset of a particular image in a sequence.

(Note that this is a step toward completing your next major code assignment)

Challenges:

Compute a reaction time from some stimulus change that is not simply the onset of an image, e.g. a change in the location of an image, a change in the color of a patch,

Record reaction times for multiple trials, save to a file *

Display an instruction screen prior to showing images, telling participants what to do in your task *

Allow participants to choose a button to use for their responses **

Implement a quit key, such that if the quit key is pressed, the experiment stops and the experiment window is closed. **
'''

#%%
# Imports
import os
import random
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from psychopy.hardware import keyboard

#%%
# set keyboard and clear buffer
kb = keyboard.Keyboard()
kb.clearEvents()


# set some necessary variables
floc_dir = 'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'
#floc_dir = 'C:/Users/gis_r/OneDrive/Documents/Python/Assignment 1/fLoc_stimuli'
tnum = 10
lr_locations = [(200,0), (-200,0), (0,0)]
img_stim = []
key_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# grab stimuli from floc_stim folder
for root, dirs, files in os.walk(floc_dir):
    for file in files:
        if file.startswith('house'):
            img_stim.append(os.path.join(floc_dir, file))


# dialogue box for user to set response and quit buttons
myDlg = gui.Dlg(title="Participation Code 3")
myDlg.addText('Please choose one key for your responses and a different key to quit the experiment at any time.')
myDlg.addField(label='Response key:', choices=key_list)
myDlg.addField(label='Quit key:', choices=key_list)
ok_data = myDlg.show()

# check that the two keys are different 
while ok_data[0] == ok_data[1]:
    myDlg = gui.Dlg(title="Participation Code 3")
    myDlg.addText('You cannot have your response and quit key be the same. Please choose two different keys.')
    myDlg.addField(label='Response key:', choices=key_list)
    myDlg.addField(label='Quit key:', choices=key_list)
    ok_data = myDlg.show()

# set the response and quit keys
key_response = ok_data[0]
key_quit = ok_data[1]

# create/append to a txt file
f = open("participation_code3.txt", "a")


# build experiment window and begin trials
try:
    fullscr = False
    screen_size = [1440,900]
    max_wait = 3
    method = 'waitKeys'
    win = visual.Window(size=(800,800),#screen_sizae,
                        color=(0.5,0.5,0.5),
                        fullscr=fullscr,
                        units='pix',)
    
    
    ###################################
    ############ TRIAL ONE ############
    
    # measure response to onset of a stimulus
    my_str = 'Press ' + key_response + ' when an image appears on the screen!'
    txt_stim = visual.TextStim(win, text=my_str)
    txt_stim.draw()
    win.flip() 
    key_out = kb.waitKeys(maxWait=5,
                          keyList=(key_quit))
    if key_out:
        f.close()
        win.close()
        core.quit()
    else:
        pass
    core.wait(5)

    f.write('\nResponse time to stimulus onset:')
    for i in range(tnum):
        img = visual.ImageStim(win,
                                random.choice(img_stim),
                                pos=(0,0),
                                size=(300,300),
                                units="pix")
        img.draw()
        win.flip()
        t1 = core.getTime()
        key_out = kb.waitKeys(maxWait=max_wait,
                                    keyList=(key_response, key_quit))
        if key_out[0] == key_quit:
            f.close()
            win.close()
            core.quit()
            
        t2 = core.getTime(key_out)

        f.write('\n ' + str(t2-t1))

    ###################################
    ############ TRIAL TWO ############
    
    # Measure response time to an event (img moves)
    my_str = 'Press ' + key_response + ' if an image moves to a new position on the screen!'
    txt_stim = visual.TextStim(win, text=my_str)
    txt_stim.draw()
    win.flip()
    key_out = kb.waitKeys(maxWait=5,
                          keyList=(key_quit))
    if key_out:
        f.close()
        win.close()
        core.quit()
    else:
        pass
    core.wait(5)

    f.write('\nResponse time to stimulus event:')
    for i in range(tnum):
        img_rand = random.choice(img_stim)
        
        img = visual.ImageStim(win,
                                img_rand,
                                pos=(0,0),
                                size=(300,300),
                                units="pix")
        img.draw()
        win.flip()
        key_out = kb.waitKeys(maxWait=5,
                              keyList=(key_quit))
        if key_out:
            f.close()
            win.close()
            core.quit()
        else:
            pass
        core.wait(1)
        
        img = visual.ImageStim(win,
                                img_rand,
                                pos=random.choice(lr_locations),
                                size=(300,300),
                                units="pix")
        img.draw()
        win.flip()
        
        t1 = core.getTime()
        key_out = kb.waitKeys(maxWait=max_wait,
                                    keyList=(key_response, key_quit))
        if key_out is None:
            pass
        elif key_out[0] == key_quit:
            f.close()
            win.close()
            core.quit()
        t2 = core.getTime(key_out)

        if t2-t1 < 3:
            f.write('\n ' + str(t2-t1))
    

except:
    win.close()
    # Raise last error
    raise


f.close()

win.close()
core.quit()
# %%
