import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2*np.exp(-x)

x = 0
dx = 1. / 100
sum = 0

for i in range(1000):
    sum = sum + f(x) * dx
    x = x + dx

print(sum)

sum = 0
x = 0
N = 10000

for i in range(N):
    r = np.random.random()
    x = - np.log(1 - r)
    sum = sum + x ** 2

print(sum / N)
