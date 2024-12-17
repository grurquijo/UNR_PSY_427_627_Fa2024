# Name: Giselle Urquijo
# Date modified: 12/16/2024

# ======================================================================================= 

#%%
# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import animation

#%%

# set range for standard deviation
num = np.linspace(.25,1,15)

# set colormap
cmap = mpl.colormaps.get_cmap('coolwarm')
c_g = cmap(num)

# set up constants
resolution = 100
amplitude = 1
x = np.linspace(-3,3,resolution)
mu = 0
sigma = .5

# plot the gaussian distributions on the same graph
for k,j in enumerate(num):
    y = amplitude * np.e ** -(((1/2) * x - mu) / (j))**2
    plt.plot(x, y, c=c_g[k])