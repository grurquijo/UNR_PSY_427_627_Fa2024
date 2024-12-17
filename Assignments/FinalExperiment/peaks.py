
#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib import animation

#%%

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

# setting sigmas and random centers/amplitudes
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
# %%
#%%

import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.patches as mpatches

cmap = matplotlib.colors.LinearSegmentedColormap.from_list('', ['lightgray','magenta'])
cmap_gray = matplotlib.colors.LinearSegmentedColormap.from_list('', ['lightgray','lightgray'])
fig,axs = plt.subplots()
plt.tick_params(left=False, right=False, bottom=False, labelleft=False, labelbottom=False)
axs.set_aspect('equal')
# circle the gaussian blobs will sit on
theta = np.linspace(0, np.pi*2, 12, endpoint=False)
m = .75 * np.cos(theta)
n = .75 * np.sin(theta)
blob_pos = np.vstack((m,n)).T


# make some small gaussian blobs
t = np.linspace(-1, 1, 100)
x, y = np.meshgrid(t, t)

def make_gauss(mu_x, mu_y, sigma, x=x, y=y):
    g = np.e**(-((x - mu_x)**2 + (y-mu_y)**2)/(2*sigma**2))
    return g

tmp = 0
for j,k in enumerate(blob_pos):
    tmp += make_gauss(m[j],n[j],.05)
axs.imshow(tmp, cmap=cmap)


circ_m = (37.5 * np.cos(theta))+50
circ_n = (37.5 * np.sin(theta))+50
gray_pos = np.vstack((circ_m,circ_n)).T

for j,k in enumerate(gray_pos):
    circ = mpatches.Circle((circ_m[j], circ_n[j]), 9, color='lightgray')#31
    axs.add_patch(circ)


plt.show()