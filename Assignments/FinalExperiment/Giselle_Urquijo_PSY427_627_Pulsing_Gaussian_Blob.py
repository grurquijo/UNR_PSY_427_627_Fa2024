# Name: Giselle Urquijo
# Date modified: 12/16/2024

# ======================================================================================= 

# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import animation


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