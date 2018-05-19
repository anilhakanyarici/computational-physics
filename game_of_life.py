import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def random_forest(size = 40, p = 0.4):
    m = np.random.random((size, size))
    for i in range(size):
        for j in range(size):
            m[i, j] = int(m[i, j] <= p)
    return m

def z():
    Z = np.zeros((4, 5))
    Z[1, 1:3] = 1
    Z[2, 2:4] = 1
    return Z

fig = plt.figure()
im = plt.imshow(random_forest())
#im = plt.imshow(z())


def neighboors_count_8(matrix, i, j): 
    UL = 0 #Kuzeybatı'daki komşu. (up-left)
    if(0 <= i - 1 and 0 <= j - 1):
        UL = matrix[i - 1, j - 1]
    U = 0 #Kuzey'deki komşu. (up)
    if(0 <= i - 1):
        U = matrix[i - 1, j]
    UR = 0 #Kuzeydoğu'daki komşu. (up-right)
    if(0 <= i - 1 and j + 1 < matrix.shape[1]):
        UR = matrix[i - 1, j + 1]
    L = 0 #Batı'daki komşu. (left)
    if(0 <= j - 1): 
        L = matrix[i, j - 1]
    R = 0 #Doğu'daki komşu. (right)
    if(j + 1 < matrix.shape[1]): 
        R = matrix[i, j + 1]
    DL = 0 #Güneybatı'daki komşu. (down-left)
    if(0 <= j - 1 and i + 1 < matrix.shape[0]): 
        DL = matrix[i + 1, j - 1]
    D = 0 #Güney'deki komşu. (down)
    if(i + 1 < matrix.shape[0]):
        D = matrix[i + 1, j]
    DR = 0 #Güneydoğu'daki komşu. (down-right)
    if(i + 1 < matrix.shape[0] and j + 1 < matrix.shape[1]):
        DR = matrix[i + 1, j + 1]
    
    return UL + U + UR + L + R + DL + D + DR

def neighboors_count_4(matrix, i, j):
    U = 0 #Kuzey'deki komşu. (up)
    if(0 <= i - 1):
        U = matrix[i - 1, j]
    L = 0 #Batı'daki komşu. (left)
    if(0 <= j - 1): 
        L = matrix[i, j - 1]
    R = 0 #Doğu'daki komşu. (right)
    if(j + 1 < matrix.shape[1]): 
        R = matrix[i, j + 1]
    D = 0 #Güney'deki komşu. (down)
    if(i + 1 < matrix.shape[0]):
        D = matrix[i + 1, j]
    
    return U + L + R + D

def start(): return [im]
def update(i):
    a = im.get_array()
    row_count = a.shape[0]
    column_count = a.shape[1]

    m = np.zeros(a.shape)

    for i in range(row_count):
        for j in range(column_count):
            T = neighboors_count_8(a, i, j)

            if(T < 2): m[i, j] = 0 #Sıkıntıdan öldü.
            if(T > 3): m[i, j] = 0 #Doğal seçilime uğradı.
            if(T == 3): m[i, j] = 1 #2'si çiftleşti, diğeri ebelik yaptı. :)
    im.set_array(m)
    return [im]

#frames = update metoduna geçirilen "i" parametresinin kaça kadar değer alacağını belirtir. frames = n ise, 0 <= i < n arasında değerler alır, sonraki frame başa döner.
#interval = 2 frame'in çizilmesi arasında geçen zaman (ms).
anim = animation.FuncAnimation(fig, update, init_func = start, frames = 1, interval = 200)
plt.show()
