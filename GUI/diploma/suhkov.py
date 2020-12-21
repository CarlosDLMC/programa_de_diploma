import matplotlib.pyplot as plt
import numpy as np

def radianes(grados):
    return grados * np.pi / 180

gr = np.linspace(0, 360, 360)
x = 10 * np.cos(radianes(gr))
y = 10 * np.sin(radianes(gr))
z = 9.7 * np.sin(radianes(gr))

fig, ax = plt.subplots(ncols=3, nrows=1, figsize=(12, 3))
ax[0].plot(x, y)
ax[0].set(title='без эксцентриситета')
ax[1].plot(x, z)
ax[1].set(title='экс = 0,97')
ax[2].plot(x, y, label='без эксцентриситета')
ax[2].plot(x, z, label='экс = 0,97')
ax[2].set(title='сравнение')
ax[2].legend()
plt.show()