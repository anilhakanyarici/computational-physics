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

def fire_tree(L, i, j): #L ormanındaki (i, j) konumundaki ağacı ve yanındakileri recursive olarak yakar. 
    t = L[i, j]
    if(t == 1):
        L[i, j] = 2
        size = L.shape[0]
        if(i + 1 < size): fire_tree(L, i + 1, j)
        if(j + 1 < size): fire_tree(L, i, j + 1)
        if(i - 1 > 0): fire_tree(L, i - 1, j)
        if(j - 1 > 0): fire_tree(L, i, j - 1)

def fire_forest(L):
    size = L.shape[0]
    for i in range(size):
        if(L[0, i] == 1): 
            fire_tree(L, 0, i)
    
    found_burned_tree = False
    for i in range(size):
        found_burned_tree = (L[i, 0] == 2)
        if(found_burned_tree): break
    if(not found_burned_tree): return False
    
    for i in range(size):
       found_burned_tree = (L[size - 1, i] == 2)
       if(found_burned_tree): break
    if(not found_burned_tree): return False

    for i in range(size):
       found_burned_tree = (L[i, size - 1] == 2)
       if(found_burned_tree): break

    return found_burned_tree
    


L = create_lattice(100, 0.6)
#Lc = copy_lattice(L)
percolated = fire_forest(L)

print("Percolated: ", percolated)

plt.imshow(L)
plt.show()