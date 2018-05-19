import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

NX = 100
NY = 100

S = np.random.random((NY, NX))
for i in range(NY):
    for j in range(NX):
        S[i, j] = 2 * int(S[i, j] <= 0.5) - 1

fig = plt.figure()
im = plt.imshow(S)

#plt.imshow(S)
#plt.show()
def start(): return [im]
def update(i):
    beta = 0.6
    h = 0
    for iy in range(NY):
        for ix in range(NX):
            S0 = S[iy, ix]
            SNx = S[iy, (ix + 1) % NX]
            SLx = S[iy, (ix - 1 + NX) % NX]
            SNy = S[(iy + 1) % NY, ix]
            SLy = S[(iy -1 + NY) % NY, ix]
            neigh = SNx + SLx + SNy + SLy
            HOld = S0 * (neigh  + h)
            HNew = -HOld
            DeltaH = HNew - HOld
            if DeltaH > 0: S[iy, ix] = -S0
            elif np.exp(beta * DeltaH) > np.random.random(): S[iy, ix] = -S0 #Termal dalgalanma
    
    im.set_array(S)
    return [im]

anim = animation.FuncAnimation(fig, update, init_func = start, frames = 1, interval = 16)
plt.show()
