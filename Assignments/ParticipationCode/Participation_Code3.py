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
import psychopy
import numpy as np
import random
import os

from psychopy import visual, core, event, gui

#%%
# variables
floc_dir = 'C:/Users/gis_r/OneDrive/Documents/Python/Assignment 1/fLoc_stimuli'
tnum = 1
lr_locations = [(200,0), (-200,0), (0,0)]
img_stim = []
key_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


for root, dirs, files in os.walk(floc_dir):
    for file in files:
        if file.startswith('house'):
            img_stim.append(os.path.join(floc_dir, file))


# dialogue box
myDlg = gui.Dlg(title="Participation Code 3")
myDlg.addText('Please choose one key for your responses and a different key to quit the experiment at any time.')
myDlg.addField(label='Response key:', choices=key_list)
myDlg.addField(label='Quit key:', choices=key_list)
ok_data = myDlg.show()

while ok_data[0] == ok_data[1]:
    myDlg = gui.Dlg(title="Participation Code 3")
    myDlg.addText('You cannot have your response and quit key be the same. Please choose two different keys.')
    myDlg.addField(label='Response key:', choices=key_list)
    myDlg.addField(label='Quit key:', choices=key_list)
    ok_data = myDlg.show()
pass

key_response = ok_data[0]
key_quit = ok_data[1]

f = open("participation_code3.txt", "a")
key_quit_pressed = event.getKeys(keyList=key_quit)

while key_quit != key_quit_pressed:
    try:
        fullscr = False
        screen_size = [1440,900]
        max_wait = 3 
        method = 'waitKeys' 
        win = visual.Window(size=(800,800),#screen_size, 
                            color=(0.5,0.5,0.5),
                            fullscr=fullscr, 
                            units='pix',)
        
        
        # time for onset of a stimulus
        my_str = 'Press ' + key_response + ' when an image appears on the screen!'
        txt_stim = visual.TextStim(win, text=my_str)
        txt_stim.draw()
        win.flip()
        core.wait(5)

        f.write('\nResponse time to stimulus onset:')
        for i in range(tnum):
            img = visual.ImageStim(win, random.choice(img_stim), pos=(0,0), size=(300,300), units="pix")
            img.draw()
            win.flip()
            t1 = core.getTime()
            key_out = event.waitKeys(maxWait=max_wait, keyList=key_response)
            t2 = core.getTime(key_out)

            f.write('\n ' + str(t2-t1))

        
        # time from when an event (img moves) occurs
        my_str = 'Press ' + key_response + ' if an image moves to a new position on the screen!'
        txt_stim = visual.TextStim(win, text=my_str)
        txt_stim.draw()
        win.flip()
        core.wait(5)

        f.write('\nResponse time to stimulus event:')
        for i in range(tnum):
            img_rand = random.choice(img_stim)
            
            img = visual.ImageStim(win, img_rand, pos=(0,0), size=(300,300), units="pix")
            img.draw()
            win.flip()
            core.wait(1)
            
            img = visual.ImageStim(win, img_rand, pos=random.choice(lr_locations), size=(300,300), units="pix")
            img.draw()
            win.flip()
            
            t1 = core.getTime()
            key_out = event.waitKeys(maxWait=max_wait, keyList=key_response)
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
