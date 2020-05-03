import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def gauss(mean, sigma, x):
    variance = sigma * sigma
    a = 1.0 / np.sqrt(2 * 3.1415 * variance)
    p = np.power((x - mean), 2) / (2 * variance)
    return a * np.exp(-p)

def gauss3(x):
    return gauss(5, 3, x) + gauss(7, 2, x) + gauss(1, 4, x)

def metropolis_hastings(p, n):
    samples = np.zeros(n)
    x_min = -15
    x_max = 15
    x = 0
    for i in range(n):
        x_post = x + np.random.random() * 2 - 1 
        while(x_post < x_min or x_max < x_post):
            x_post = x + np.random.random() * 2 - 1 
        if np.random.rand() < np.minimum(1, p(x_post) / p(x)):
            x = x_post
        samples[i] = x

    return samples

def F(x):
    return (x * x + 1) * np.exp(-x * x)
    #return np.sqrt(x + 1)

samples = metropolis_hastings(gauss3, 100000)
print(np.sum(F(samples)) / samples.size)
plt.hist(samples, bins = 250)
plt.show()

