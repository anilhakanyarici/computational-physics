import numpy as np
import matplotlib.pyplot as plt

def create_lattice(size, probability):
    L = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            L[i, j] = int(probability > np.random.random())
    return L

def copy_lattice(L): #deep copy
    size = L.shape[0]
    Lc = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            Lc[i, j] = L[i, j]
    return Lc

def label_cluster(L, i, j, label): #
    t = L[i, j]
    if(t == 1):
        L[i, j] = label
        size = L.shape[0]
        if(i + 1 < size): label_cluster(L, i + 1, j, label)
        if(j + 1 < size): label_cluster(L, i, j + 1, label)
        if(i - 1 > 0): label_cluster(L, i - 1, j, label)
        if(j - 1 > 0): label_cluster(L, i, j - 1, label)

def count_clusters(L):
    size = L.shape[0]
    label = 2
    for i in range(size):
        for j in range(size):
            if(L[i, j] == 1): 
                label_cluster(L, i, j, label)
                label = label + 1
    return label - 2 #kluster kount
    



L = create_lattice(100, 0.592746)
cc = count_clusters(L)
print("Cluster count: ", cc)

plt.imshow(L)
plt.show()