# Name: Giselle Urquijo
# Date Modified: 12/16/2024

# Extra credit: 1 and 3

#%%
# imports
import os
import numpy as np
import psychopy

from psychopy import visual, core, event

# %%
'''
Lilac Chaser in Psychopy
'''
# variables
window_up = 5
n_blobs = 12
circ_rad = 150
wait_time = 0.10

# setting screen
screen_size = [400,400]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

# setting fixation point
fixation = visual.ShapeStim(win, 
                            vertices=((0, -7), (0, 7), (0,0), (-7,0), (7, 0)),
                            lineWidth=.75,
                            closeShape=False,
                            lineColor='black')

# circle points
theta = np.linspace(0, np.pi*2, 12, endpoint=False)
x = np.flip(circ_rad * np.cos(theta))
y = np.flip(circ_rad * np.sin(theta))

# loop through for window_up time
time = 0
while time < window_up:
    for j in range(n_blobs):
        
        # draw all the blobs
        for i in range(n_blobs):
            blob = visual.GratingStim(win=win, mask='gauss', units='pix', size=50, sf=50,color='magenta', pos=(x[i],y[i]))
            blob.draw()
        
        # draw the blob that blocks one of the pink blobs
        blob_gray = visual.Circle(win=win, units='pix', radius=50, fillColor=(0.5,0.5,0.5), pos=(x[j],y[j]))
        blob_gray.draw()
        #draw fixation
        fixation.draw()
        win.flip()
        core.wait(wait_time)
        
    time += (wait_time*n_blobs)

win.close()
core.quit()
# %%
'''
Click and drag images around 
'''
# number of stimuli to rearrange and length of experiment in seconds
n_stim = 3
exp_time = 15

# stimuli location and setup         
stim_loc = 'C:/Users/Giselle/Documents/python/UNR/fLoc_stimuli'

stim = []
for root, dirs, files in os.walk(stim_loc):
    for file in files:
        stim.append(os.path.join(stim_loc, file))
        
stim = np.random.choice(stim, n_stim, replace=False)

# setting screen and mouse
screen_size = [1000,600]
win = visual.Window(size=screen_size, 
                    color=(0.5,0.5,0.5),
                    fullscr=False, 
                    units='pix')

mouse = event.Mouse(newPos=(0,0),
                    win=win)

# awful math to get evenly spread x positions depending on width of screen. Can work with fullscreen, 
#       but screen_size still has to have a value assigned to it. Also a lil funky with only 1 image.
pos_x = np.linspace((-(screen_size[0]/2 - 150)), ((screen_size[0]/2 - 150)), n_stim)

# draw stimuli in initial positions
img_stim =[]
for i in range(n_stim):
    img = visual.ImageStim(win, 
                           stim[i], 
                           pos=(pos_x[i], 0), 
                           size=(150,150))
    img_stim.append(img)
    img.draw()

message = visual.TextStim(win, 
                          pos=(0, (screen_size[1]/2 - 20)), 
                          text='Click and Drag the images. You have ' + str(exp_time) + ' seconds.')

message.draw()
win.flip()

# grab time
clock = core.Clock()
t1 = clock.getTime()
t = 0

# click and drag images during the specified amount of time
while t < t1 + exp_time:
    # check every image >> if mouse is clicked inside one of the images update image position with mouse position
    for i in img_stim:
        if mouse.isPressedIn(i):
            i.pos = mouse.getPos()
        else:
            pass
        
    # redraw stimuli with updated positions        
    for i in img_stim:
        i.draw()
        
    message.draw()
    win.flip()
    t = clock.getTime()
    

win.close()
core.quit()
# %%
