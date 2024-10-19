#%%
# Imports
import os
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from psychopy.hardware import keyboard
from experiment1_functions import *


#%%
# set keyboard and clear buffer
kb = keyboard.Keyboard()
kb.clearEvents()


floc_dir = 'C:/Users/gis_r/Documents/Python/Assignment 1/fLoc_stimuli'
key_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


fullscr = True
max_wait = .5
method = 'waitKeys'
win = visual.Window(color=(0.5,0.5,0.5),
                    fullscr=fullscr,
                    units='pix',)

##############################################################
######################### DIALOG BOX #########################
##############################################################

myDlg = gui.Dlg(title="Experiment 1")
myDlg.addText('In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images.'
                '\n\nAs you watch the images go by, please press your chosen response button as fast as you can if you see a repeated image.')
ok_data = myDlg.show()

myDlg = gui.Dlg(title="Experiment 1")
myDlg.addText('Please choose one key for your responses and a different key to quit the experiment at any time.')
myDlg.addField(label='Response key:', choices=key_list)
myDlg.addField(label='Quit key:', choices=key_list)
ok_data = myDlg.show()


# make sure the response and quit keys are not the same. If they >> request them again
while ok_data[0] == ok_data[1]:
    myDlg = gui.Dlg(title="Participation Code 3")
    myDlg.addText('You cannot have your response and quit key be the same. Please choose two different keys.')
    myDlg.addField(label='Response key:', choices=key_list)
    myDlg.addField(label='Quit key:', choices=key_list)
    ok_data = myDlg.show()


# set the response and quit keys

key_response = ok_data[0]
key_quit = ok_data[1] 

# grab stimuli
faces = []
find_files(floc_dir, 'adult', 'child', faces)

places = []
find_files(floc_dir, 'house', 'corridor', places)

objects = []
find_files(floc_dir, 'instrument', 'car', objects)





fid = open("./Data_Collected/experiment1_data.txt", "a")

trial(win, 1, 20, faces, key_response, key_quit, fid, max_wait, kb)
block_pause()

trial(win, 2, 20, places, key_response, key_quit, fid, max_wait, kb)
block_pause()

trial(win, 3, 20, objects, key_response, key_quit, fid, max_wait, kb)
block_pause()



fid.close()
win.close()
core.quit()


# %%
