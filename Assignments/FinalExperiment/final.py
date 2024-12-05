# Name: Giselle Urquijo
# Date modified: 12/3/2024

#%%
# imports
import numpy as np
import matplotlib.pyplot as plt

#%%

num = np.linspace(.25,1,15)

resolution = 100
amplitude = 6
x = np.linspace(-3,3,resolution)
mu = 0
sigma = .5
for j in num:
    y = amplitude * np.e ** -(((1/2) * x - mu) / (j))**2
    plt.plot(x, y)

#%%

