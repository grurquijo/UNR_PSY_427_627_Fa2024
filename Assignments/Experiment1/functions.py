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
  
def check_keypress(max_wait,key_r, key_q,f,win):
    key_out = event.waitKeys(maxWait=max_wait)
    if not key_out:
        pass
    elif key_out == key_r:
        f.write('oop')
    elif key_out == key_q:
        f.close()
        win.close()
        core.quit()
           
def trial(win, block_num, tnum, array, key_r, key_q, f, max_wait):
    try:
        f.write('\n Block ' + str(block_num) + ':' )
        exp1_clock = core.Clock()
        imgs_in_trial = []
        for i in range(tnum):
            
            circ_stim = visual.Circle(win, radius=7.5,
                              units='pix',
                              fillColor=('yellow'),
                              pos=(0,0))
                        
            rand_img = np.random.choice(array)
            imgs_in_trial.append(rand_img)

            img = visual.ImageStim(win, 
                                   rand_img, 
                                   pos=(0,0), 
                                   size=(500,500), 
                                   units="pix")
            
            img.draw()
            circ_stim.draw()

            win.flip()
            
            exp1_clock.reset(newT=0.0)
            t1 = exp1_clock.getTime()
            
            key_out = event.waitKeys(maxWait=max_wait)
            
            t2 = exp1_clock.getTime(key_out)
            
            if not key_out:
                pass
            elif key_out == key_r:
                f.write('\nTrial ' + str(i) + ': ' + str(key_out)+ ', ' + str(t2-t1) + rand_img)
            elif key_out == key_q:
                f.close()
                win.close()
                core.quit()
            
            #core.wait(.5)
            core.wait(0.1)     
            
            img_t2 = exp1_clock.getTime() 
            f_img_time = open("./Data_Collected/stimuli_timing.txt", "a")
            f_img_time.write(str(img_t2-t1)+"\n")

        
    except:
        win.close()
        # Raise last error
        raise
    f.write('\nImages in Block ' + str(block_num) + ':')
    for img_stim in imgs_in_trial:
        f.write('\n' + img_stim)


