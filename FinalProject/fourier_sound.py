# Fourier sound demo
# Sounds can be downloaded from piecesofmind.psyc.unr.edu/data/animal_sounds.tar.gz; they must be unzipped! 
#%% Imports
from psychopy import sound
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation 
import os

#%% Load sound
fdir = 'C:/Users/gis_r/Documents/Python/Assignment 1/animal_sounds'
Snd = sound.Sound(os.path.join(fdir, 'horse.mp3'))

fs = Snd.sampleRate
y = Snd.sndArr.flatten()
t = np.arange(0, Snd.duration, 1/fs)
plt.plot(t, y)

fig,axs = plt.subplots()

N = len(y)
T = len(y)/fs
p_orig = np.abs(np.fft.fft(y)) / (N / 2) 
p = p_orig[:int(np.ceil(N/2))] # **2? # take the power of positve freq. half 
freq = np.arange(N/2) / T # [0:N/2-1]/T ## find the corresponding frequency in Hz 


# line plot that updates from the fourier transform window sliding 