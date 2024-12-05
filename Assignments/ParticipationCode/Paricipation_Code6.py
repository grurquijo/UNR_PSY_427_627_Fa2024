#%%
import numpy as np
import matplotlib.pyplot as plt

freq = 3

x = np.linspace(0,2*np.pi, 100)

n_waves = 10
colors = plt.cm.viridis(np.linspace(0,1,n_waves))
amplitudes = np.linspace(0.5, 2, n_waves)
for j in range(n_waves):
    amplitude = amplitudes[j]
    color = colors[j]
    y = amplitude * np.sin(freq*x)

    plt.plot(x,y,'-')

plt.xlim([0,2*np.pi])
plt.ylim([-2.25,2.25])

#%%
resolution = 100
amplitude = 6
x = np.linspace(-3,3,resolution)
mu = 0
sigma = .5
y = amplitude * np.e ** -(((1/2) * x - mu) / (sigma))**2

plt.plot(x, y)