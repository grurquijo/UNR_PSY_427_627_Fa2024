# Name: Giselle Urquijo
# Date modified: 12/16/2024

# ======================================================================================= 

# imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import animation


fig = plt.figure()

# figure cleanup
axs = fig.add_subplot(111, projection='3d')
axs.tick_params(left=False, right=False, bottom=False, labelleft=False, labelbottom=False)
axs.grid(False)
axs.set_xticks([])
axs.set_yticks([])
axs.set_zticks([])
axs.set_xlim([-10,10])
axs.set_ylim([-10,10])
axs.set_zlim([0,40])


# number of gaussians and frames
num = 16
n_frames = num * 4

# set up messhgrid
t = np.linspace(-10, 10, 100)
x, y = np.meshgrid(t, t)

# setting sigmas and randome centers/amplitudes
v = np.random.randint(-10,10,num)
w = np.random.randint(-10,10,num)
u = np.random.randint(4,7,num)

v = np.repeat(v, 4)
w = np.repeat(w, 4)
u = np.repeat(u, 4)

some_sig = np.linspace(0,1,num)
some_sig = np.repeat(some_sig, 4)

# gaussiannnnn
def make_gauss(amp, mu_x, mu_y, sigma, x=x, y=y):
    g = amp * (np.e**(-((x - mu_x)**2 + (y-mu_y)**2)/(2*(sigma)**2)))
    return g

# initial "empty" plot
g = make_gauss(.001,0,0,.001)
blob_empty = axs.plot_surface(x, y, g, cmap='viridis')
blob_peak = 0

# update every frame
def update(frame):
    global blob_empty, blob_peak
    blob_peak += make_gauss(u[frame],v[frame],w[frame],some_sig[frame:frame+1])
    blob_empty.remove()
    blob_empty = axs.plot_surface(x, y, blob_peak, cmap='viridis')
    return blob_empty,

# create the animation and save
ani = animation.FuncAnimation(fig=fig, func=update, frames=n_frames, interval=100)

plt.show()
ani.save('./3D_gaussian_peaks.mp4', writer='ffmpeg')