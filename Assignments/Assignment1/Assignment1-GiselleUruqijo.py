# Name: Giselle Urquijo
# Date Modified: 9/16/2024

#%% Imports

import numpy as np
import os
import matplotlib.pyplot as plt
from os import listdir


# Current pathway
curDir = os.path.abspath(os.curdir)
flocDir = os.path.join(curDir, 'fLoc_stimuli')


# variables
#flocDir = 'C:/Users/gis_r/OneDrive/Documents/Python/Assignment 1/fLoc_stimuli'
myList = os.listdir(flocDir)
myPick = np.random.randint(np.size(myList), size=12)
myArray = []


# no ticks on figres pls and ty
def noTicks():
    plt.setp(axs, xticks=[], yticks=[])


# creating array of images and iterate through them one by one
for i in myPick:
    myArray.append(myList[i])
    #myArray.append(os.path.join(flocDir, myList[i]))
    im = plt.imread(os.path.join(flocDir, myList[i]))
    plt.imshow(im, cmap='gray')
    plt.show()


# figure of the random images in one figure in order
fig, axs = plt.subplots(12, 1, figsize=(50,50))
noTicks()
for i, ax in enumerate(axs.flatten(), 1):
    im = plt.imread(os.path.join(flocDir, myArray[i - 1]))
    ax.imshow(im, cmap='gray')


# figure of the random images in a 4x3 grid
fig, axs = plt.subplots(4, 3, figsize=(10,10))
noTicks()
for i, ax in enumerate(axs.flatten(), 1):
    im = plt.imread(os.path.join(flocDir, myArray[i - 1]))
    ax.imshow(im, cmap='gray')


# save the array as randomly_selected_images and load into myArrayLd
np.save('randomly_selected_images.npy', myArray)
myArrayLd = np.load('randomly_selected_images.npy')


# %%
