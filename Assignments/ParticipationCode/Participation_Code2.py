# Name: Giselle Urquijo
# Date modified: 10/1/2024

#%% imports
import psychopy
import numpy as np
import os
import matplotlib.pyplot as plt
from psychopy import visual, core

#%%
my_clock = psychopy.clock.Clock()
t0 = my_clock.getTime()
test = 100
tms = np.zeros((test, ))
wait_time = .1

for repeat in range(test):
    t1 = my_clock.getTime(); 
    core.wait(wait_time); 
    t2 = my_clock.getTime()
    chg_time = (t2-t1)
    tms[repeat] = chg_time

#%%
tms_std = np.std(tms)
print(tms_std)

# %%
screen_size = [400,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

flip1 = win.flip()
core.wait(.005)
flip2 = win.flip()
win.close()

time_delta = flip2 - flip1
# %%
