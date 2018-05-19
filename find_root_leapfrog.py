import math
import numpy as np

def f(omega):
    L = 1.0
    NSteps = 1000
    L = 1.0
    dx = L / NSteps
    x = 0.0
    s1 = 0
    s2 = 0
    while(x <= L/2):
        s1 = math.sin(x * omega)
        s2 = math.sin((L - x) * omega)
        x = x + dx
    return s1 - s2

def findRoot(f, x0, eps):
    x = x0
    dx = 0.001
    while(math.fabs(f(x)) > eps):
        xn = x - 2 * dx * f(x) / (f(x + dx) - f(x - dx))
        x = xn
    return x

r = findRoot(f, 1.8, 0.0001)
print(r / math.pi)
