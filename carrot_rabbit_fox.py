import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

soil = 0 #MOR
carrot = 1 #MAVİ
rabbit = 2 #YEŞİL
fox = 3 #SARI

size = 80
soil_probability = 0.05
carrot_probability = 0.2
rabbit_probability = 0.5
fox_probability = 1 - (carrot_probability + rabbit_probability + soil_probability)

carrot_spoil_probability = 0.3
rabbit_death_probability = 0.5
fox_death_probability = 0.2

'''
Kurallar:
1) Seçilen hücre soil ise orada carrot, rabbit veya fox oluşabilir. "carrot_probability" ihtimalle carrot oluşur, oluşmaz ise 2. ve 3. kurala göre rabbit veya fox çıkar.
2) Komşulardan en az 2 tanesi rabbit ve en az 1 tanesi carrot ise ve hücre de soil ise orada rabbit doğar.
3) Komşulardan en az 2 tanesi fox ve en az 1 tanesi rabbit ise ve hücre de soil ise orada fox doğar.
4) Seçilen hücre carrot ise:
    en az 1 komşusu rabbit ise, hücre soil olur.
    "carrot_spoil_probability" ihtimalle çürür, hücre soil olur.
5) Seçilen hücre rabbit ise:
    en az 1 komşusu fox ise, hücre soil olur.
    etrafında hiç carrot yok ise "rabbit_death_probability" ihtimalle ölür, hücre soil olur.
6) Seçilen hücre fox ise:
    etrafında hiç rabbit yok ise "fox_death_probability" ihtimalle ölür, hücre soil olur.
'''

M = np.random.random((size, size))
for i in range(size):
    for j in range(size):
        if(M[i, j] < soil_probability):
            M[i, j] = soil
        elif(soil_probability < M[i, j] and M[i, j] <= soil_probability + carrot_probability):
            M[i, j] = carrot
        elif(soil_probability + carrot_probability < M[i, j] and M[i, j] < carrot_probability + rabbit_probability + soil_probability):
            M[i, j] = rabbit
        else: 
            M[i, j] = fox
def get_neighboors_count(matrix, i, j):
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
    
    neighs = (U,R,L,D,UL,UR,DL,DR)
    carrot_count = 0
    rabbit_count = 0
    fox_count = 0

    for i in range(8): 
        if(neighs[i] == carrot): 
            carrot_count += 1
    for i in range(8): 
        if(neighs[i] == rabbit): 
            rabbit_count += 1
    for i in range(8): 
        if(neighs[i] == fox): 
            fox_count += 1

    return carrot_count, rabbit_count, fox_count

fig = plt.figure()
im = plt.imshow(M)
def start(): return [im]
def update(i):
    a = im.get_array()
    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            m[i, j] = a[i, j]

    for i in range(size):
        for j in range(size):
            carrot_count, rabbit_count, fox_count = get_neighboors_count(a, i, j)
            if(a[i, j] == soil):
                if((np.random.random() <= carrot_probability)): m[i, j] = carrot
                elif(rabbit_count >= 2 and carrot_count >= 1): m[i, j] = rabbit
                elif(fox_count >= 2 and rabbit_count >= 1): m[i, j] = fox
            elif(a[i, j] == carrot and rabbit_count > 0 and np.random.random() <= carrot_spoil_probability): m[i, j] = soil
            elif(a[i, j] == rabbit): 
                if(fox_count > 0): m[i, j] = soil
                elif(carrot_count == 0 and np.random.random() <= rabbit_death_probability): m[i, j] = soil                        
            elif(a[i, j] == fox and rabbit_count == 0 and np.random.random() <= fox_death_probability): m[i, j] = soil
    im.set_array(m)
    return [im]

anim = animation.FuncAnimation(fig, update, init_func = start, frames = 1, interval = 16)
plt.show()
