import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np

def func(y0, t):
    y = y0[0]
    v = y0[1]
    k = 1
    dy = v
    dv = -k * y
    return dy, dv

y0 = [1, 0]
t = np.linspace(0, 10, 100)
Y = spi.odeint(func, y0, t)

plt.plot(t, Y)
plt.show()
