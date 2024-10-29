# name: Giselle URrquijo
# date modified: 10/24/24
from psychopy import event, core, visual

def check_keypress(key_out, key_r, key_q, f, win):
    if not key_out:
        pass
    elif key_out == key_r:
        f.write('oop')
    elif key_out == key_q:
        f.close()
        win.close()
        core.quit()
    return True

t0 = core.getTime()
def trial (win, f, image, onset, offset, repeat, block_type):
    #load image
    img = visual.ImageStim(win, 
                        image, 
                        pos=(0,0), 
                        size=(500,500), 
                        units="pix") 
    circ_stim = visual.Circle(win, radius=7.5,
                              units='pix',
                              fillColor=('yellow'),
                              pos=(0,0))
    #draw image
    img.draw
    #draw fixation
    circ_stim.draw

    #waits for onset time)
    core.wait(onset)

    #look for responses
    key_out = event.getKeys()
    key_t1 = core.getTime(key_out)
    #check for quit key
    key_check = check_keypress(key_out)
    if key_check:
        key_t2 = core.getTime()
        f.write('\n' + str(key_t2 - key_t1))

    #flip @onset
    #(wait for responses) >> flip after a certaint amount of time
    win.flip()
    img_t1 = core.getTime()
    key_out = event.getKeys()
    check_keypress(key_out)
    core.wait(offset)
    #flip @offset


    return True



# delta_t = t2-t1
# if t2-t1 <0.5:
#       core.wait(0.5-delta_t)