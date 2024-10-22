
import os
import psychopy
import numpy as np
import itertools

from psychopy import visual, core, event, gui
from psychopy.hardware import keyboard


# Function

def find_files(path, opt1, opt2, empty_list):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith(opt1) or file.startswith(opt2):
                empty_list.append(os.path.join(path, file))


# circle stim
def fixation_point(win, color:str):
    circ_stim = visual.Circle(win, radius=7.5,
                              units='pix',
                              fillColor=(color),
                              pos=(0,0))
    return circ_stim


def trial(win, block_num, tnum, array, key_r, key_q, f, max_wait):
    kb = keyboard.Keyboard()
    kb.clearEvents()
    try:
        f.write('\n Block ' + str(block_num) + ':' )
        imgs_cycled_through = []
        for i in range(tnum):
            
            circ_stim = visual.Circle(win, radius=7.5,
                              units='pix',
                              fillColor=('yellow'),
                              pos=(0,0))

            img = visual.ImageStim(win, 
                                   np.random.choice(array), 
                                   pos=(0,0), 
                                   size=(500,500), 
                                   units="pix")
            
            img.draw()
            circ_stim.draw()

            win.flip()
            t1 = core.getTime()
            key_out = kb.waitKeys(maxWait=max_wait, 
                                  keyList=(key_r, key_q))
            
            t2 = core.getTime()
            
            if not key_out:
                pass
            elif key_out[0] == key_q:
                f.close()
                win.close()
                core.quit()
            else:
                f.write('\n Key Pressed:' + str(key_out[0]) + ', ' + str(t2-t1))
      
                circ_stim = visual.Circle(win, radius=7.5,
                        units='pix',
                        fillColor=('red'),
                        pos=(0,0))
                circ_stim.draw()
                win.flip
                core.wait(2)
                
            imgs_cycled_through.append(img)
            
            core.wait(.5)

            core.wait(0.1)     
            
            img_t2 = core.getTime() 
    except:
        win.close()
        # Raise last error
        raise

# three second pause between blocks :)
def block_pause(win):
    fixation_point(win,'yellow')
    win.flip()
    core.wait(.5)




