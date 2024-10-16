import os
import psychopy
import numpy as np

from psychopy import visual, core, event, gui
from psychopy.hardware import keyboard


# Function

def find_files(path, opt1, opt2, empty_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(opt1) or file.startswith(opt2):
                empty_list.append(os.path.join(path, file))


def trial(win, block_num, tnum, array, key_r, key_q, f, max_wait, kb):
    for i in range(tnum):
        img = visual.ImageStim(win, np.random.choice(array, replace=False), pos=(0,0), size=(500,500), units="pix")
        img.draw()

        fixation_point(win, 'yellow')

        win.flip()
        t1 = core.getTime()
        key_out = kb.waitKeys(maxWait=max_wait,
                                    keyList=(key_r, key_q))
        if key_out[0] == key_q:
            f.close()
            win.close()
            core.quit()
            
        t2 = core.getTime(key_out)
        f.write('\n Block ' + str(block_num) + ':' + '\n Key Pressed:' + str(key_out) + ',' + str(t2-t1))

        core.wait(.5)

        core.wait(0.1)      

# three second pause between blocks :)
def block_pause(win):
    fixation_point(win,'yellow')
    win.flip()
    core.wait(.5)


# circle stim
def fixation_point(win, color:str):
    circ_stim = visual.Circle(win, radius=7.5,
                              units='pix',
                              fillColor=(color),
                              pos=(0,0))
    circ_stim.draw()