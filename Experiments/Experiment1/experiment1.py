
#%%
# Imports
import os
import random
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from psychopy.hardware import keyboard


key_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


fullscr = True
# screen_size = [1440,900]
max_wait = 3
method = 'waitKeys'
win = visual.Window(# size=screen_size,
                    color=(0.5,0.5,0.5),
                    fullscr=fullscr,
                    units='pix',)

myDlg = gui.Dlg(title="Experiment 1")
myDlg.addText('In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images.'
                '\nAs you watch the images go by, please press your chosen response button as fast as you can if you see a repeated image.')
ok_data = myDlg.show()

myDlg = gui.Dlg(title="Experiment 1")
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


# set the response and quit keys
key_response = ok_data[0]
key_quit = ok_data[1]

circ_stim = visual.Circle(win, radius=12,
                              units='pix',
                              fillColor=(1.0, 0.0, 0.0),
                              pos=(0,0))
circ_stim.draw()
win.flip()
core.wait(5)




win.close()
core.quit()
# %%
