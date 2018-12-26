import matplotlib.pyplot as plt
import numpy as np
    
#a and b are integral regions of function of f.
#n is term number of fourier series
def an(n, a, b, f):
    p = b - a
    dx = 0.05
    integral = 0
    twopi = 2 * np.pi
    for x in np.arange(a, b, dx):
        integral += f(x) * np.cos(twopi * n * x / p) * dx
    integral = 2 * integral / p
    return integral
def bn(n, a, b, f):
    p = b - a
    dx = 0.05
    integral = 0
    twopi = 2 * np.pi
    for x in np.arange(a, b, dx):
        integral += f(x) * np.sin(twopi * n * x / p) * dx
    integral = 2 * integral / p
    return integral

#x is domain of f and fourier_series(x)
#N is iteration number of sum of series.
#a and b are integral regions of function of f.
#For higer value of N, fourier_series(x) must be equal to f(x) approximately.
def fourier_series(x, a, b, N, f):
    s = an(0, a, b, f) / 2
    twopi = 2 * np.pi
    p = b - a
    for i in range(1, N):
        s += an(i, a, b, f) * np.cos(twopi * i * x / p) + bn(i, a, b, f) * np.sin(twopi * i * x / p)
    return s 

def f(x):
    return (x - x**2) * np.exp(-2*x)

x = np.arange(0, 10, 0.05)

function = f(x)

sum_of_series = []
iteration = 10
for i in x:
    t = fourier_series(i, 0, 10, iteration, f)
    sum_of_series.append(t)
    
plt.plot(x, function, label = "function")
plt.plot(x, sum_of_series, label = "fourier series")
plt.legend()
plt.show()
