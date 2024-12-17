# Name: Giselle Urquijo
# Date modified: 12/16/2024

# ======================================================================================= 

# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import animation


fig, axs = plt.subplots()

# set bell curve
resolution = 101
amplitude = 1
t_star = np.linspace(-3,3,resolution)
mu = 0
sigma = .75
z_star = amplitude * np.e ** -(((1/2) * t_star - mu) / (sigma))**2
plt.plot(t_star,z_star)

# graph labels
axs.set(xlim=[-3, 3], ylim=[0,1.05], xlabel='X', ylabel='Y')

# make a sin wave to use the resulting points for the speed of the dot
freq = 1
u = np.linspace(0, 2 * np.pi, resolution)
v = -3 * np.sin(freq * u)

# gaussian path dot travels on using the sin wave results
mu = 0
sigma = .75
z = amplitude * np.e ** -(((1/2) * v - mu) / (sigma))**2

# set the dot
dot_maybe = axs.plot([],[],'o', color='tab:blue')[0]

# update every frame 
def update(frame):
    dot_maybe.set_xdata(v[frame:frame+1])
    dot_maybe.set_ydata(z[frame:frame+1])
    
    return (dot_maybe,)

# create animation and save
ani = animation.FuncAnimation(fig=fig, func=update, frames=101, interval=30)

plt.show()
ani.save('./dot_on_gaussian_dist.mp4', writer='ffmpeg')