'''
Pseudo-code for lilac chaser extra credit:

>> how much detail do you need for an outline? does pseudocode need to be 
>> 
the circle has 1 rotation persecond >> 65 frames in 1 second (screen refresh rate)

set krypress
create a gray window
draw fixation point
grab time
while time < time + 30:
    time += 1
    draw 11 lilac dots in a circle with one missing ( 12 spaces in total around the circle)
    flip
    wait 1/65 s
    draw same circle shift 1/12 around
    flip
    wait 1/65s

psychopy has a class to create blobs   

'''
#%%
tnum = 10
while tnum > 0:
    print('hello, world: ' + str(tnum))
    tnum -= 1