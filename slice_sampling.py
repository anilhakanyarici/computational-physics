import numpy as np
import matplotlib.pyplot as plt

def slice_sampling(funcP, xmin, xmax, w):
    X = []
    for i in range(10000):
        x = xmin + np.random.rand() * (xmax - xmin)
        y = funcP(x)
        u = np.random.rand() * y
        r = np.random.rand()
        xl = x - r * w
        xr = x + (1-r) * w
        selected = False
        while(not selected):
            while(funcP(xl) > u):
                xl -= w
            while(funcP(xr) > u):
                xr += w

            xc = xl + np.random.rand() * (xr - xl)
            if(funcP(xc) > y):
                X.append(x)
                xmin = xl
                xmax = xr
                selected = True
            else:
                if(xc > x):
                    xr = xc
                else:
                    xl = xc
    return X

mu = [5,7,1]
sigma = [3,2,4]
def g123(x):
    g1 = np.exp(-(x - mu[0])**2 / (2 * sigma[0]**2))
    g2 = np.exp(-(x - mu[1])**2 / (2 * sigma[1]**2)) 
    g3 = np.exp(-(x - mu[2])**2 / (2 * sigma[2]**2))
    return g1 + g2 + g3

plt.hist(slice_sampling(g123, 0, 10, 0.1), bins = 100)
plt.show()
