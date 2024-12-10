# Name: Giselle Urquijo
# Date modified: 12/9/2024

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
amplitude = 6
x = np.linspace(-3,3,resolution)
mu = 0
sigma = .5

# plot the gaussian distributions on the same graph
for k,j in enumerate(num):
    y = amplitude * np.e ** -(((1/2) * x - mu) / (j))**2
    plt.plot(x, y, c=c_g[k])

# =======================================================================================
#%%
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

# =======================================================================================  
# %%
fig, axs = plt.subplots()

# set up plot preferences and meshgrid for gaussian
plt.tick_params(left=False, right=False, bottom=False, labelleft=False, labelbottom=False)
t = np.linspace(-1, 1, 100)
x, y = np.meshgrid(t, t)

# set up sin wave for blob pulse speed
freq = 1
u = np.linspace(0, 2 * np.pi, 100)
v = np.abs(np.sin(freq * u))

# function to calculate the guassian at blob sin speed
def make_gauss(mu_x, mu_y, sigma, x=x, y=y):
    g = np.e**(-((x - mu_x)**2 + (y-mu_y)**2)/(2*sigma**2))
    return g

# setting center for animation
j = np.zeros(100)
k = np.zeros(100)

# actual gaussian
blob_maybe = axs.imshow(make_gauss(j,k,v), cmap='viridis')

# update size of gaussian every frame
def update(frame):
    blob_maybe = axs.imshow(make_gauss(j,k,v[frame:frame+1]), cmap='viridis')
    return blob_maybe,

# create the animation and save
ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=30)

plt.show()
ani.save('./gaussian_pulse.mp4', writer='ffmpeg')

# ======================================================================================= 
# %%
