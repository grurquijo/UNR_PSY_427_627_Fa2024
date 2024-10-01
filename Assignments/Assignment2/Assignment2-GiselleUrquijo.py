#%%Imports 
from psychopy import visual, core
import os
import matplotlib.pyplot as plt
import numpy as np

#%% Set up screen

# Create a small screen window, 
screen_size = [800,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

floc_dir = 'C:/Users/gis_r/OneDrive/Documents/Python/Assignment 1/fLoc_stimuli';
my_list = os.listdir(floc_dir)
my_pick = np.random.randint(np.size(my_list), size=12)
myArray = []

for i in my_pick:
    myArray.append(os.path.join(floc_dir, my_list[i]))

message = visual.TextStim(win, text='Ready?', color=(78, 171, 161))
# Automatically draw every frame
message.autoDraw = True  
win.flip()
core.wait(1.0)
# Change properties of existing stim
message.text = 'Of course you are.'  
win.flip()
core.wait(1.0)

message.text = 'GO'  
win.flip()
core.wait(1.0)

message.text = ' '  
win.flip()
core.wait(.01)

fig, axs = plt.subplots(1, 3, figsize=(100,100))
for i, ax in enumerate(axs.flatten(), 1):
    im = plt.imread(os.path.join(floc_dir, myArray[i - 1]))
    im.draw()
    win.flip()
    core.wait(1.0)

win.close()

# %%
