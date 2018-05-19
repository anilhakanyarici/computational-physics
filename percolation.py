import matplotlib.pyplot as plt
import numpy as np

NSize = 10
p = 0.6
M = np.zeros((NSize, NSize))
for i in range(NSize):
    for j in range(NSize):
        if p > np.random.random() : M[i, j] = 1

plt.imshow(M)
plt.show()
