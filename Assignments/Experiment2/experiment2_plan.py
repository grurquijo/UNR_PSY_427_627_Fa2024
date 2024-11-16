import os
import json

from psychopy import gui
# use dialogue box to create experiments


exp1_message = visual.TextStim(win, text='In this experiment, you will see images of faces, places, bodies, objects, and text, along with scrambled images.'
                '\n\nAs you watch the images go by, please press your chosen response button as fast as you can if you see a repeated image.')
exp1_message.draw()
win.flip()
core.wait(10)


keys_equal = True

while keys_equal:
    message = visual.TextStim(win, text='Please choose one key for your responses and a different key to quit the experiment at any time.')

    message.setAutoDraw(False)
    message.draw()
    win.flip()
    core.wait(4.0)

    message.setText('Choose a response key.') 
    message.draw()
    win.flip()
    key_response = event.waitKeys(clearEvents=True) 

    message.setText('Choose a quit key.' )
    message.draw()   
    win.flip()
    key_quit = event.waitKeys(clearEvents=True) 
    
    if key_response == key_quit:
        win.flip()
        pass
    else:
        win.flip()
        keys_equal = 
        
# you can get dialogue from dict and responses save to a list
# json writer and parser DO IT BITCH THIS IS THE PLACE TO DO IT
# save plan to json bc it can be opened with other languages and pickle can be big

# use dialogue box to get information about:
#       - use default trial, edit existing, or create new
#           > unique name or generated name
#       - name of folder where stimuli exist 
#           > warn that stimuli should all be in the same folder and uniquely named 
#           > will search for directory location
#       -f for new trial (define what a trial consists of):
#           > screen size and screen color
#           > number of trials
#           > because this is a two alternative forced comparison experiment 
#               >> what two categories are we comparing/are we comparing just from the same category
#           > duration of stimulus and max_wait time
#           