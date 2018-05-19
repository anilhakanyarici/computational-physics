import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

NX = 64
NY = 64
Volume = NX * NY
Termalization = 1000
Measurement = 100
beta = 0.3
h = 0

S = np.random.random((NY, NX))
for i in range(NY):
    for j in range(NX):
        S[i, j] = 2 * int(S[i, j] <= 0.5) - 1

def update(beta, h):
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
    
    return np.sum(S) / Volume

#Spins = np.zeros(Termalization)
#Time = np.zeros(Termalization)
Beta = np.zeros(10)
Measurements = np.zeros(10)

for b in range(10):
    for i in range(Termalization): #Dinamik bölge
        s = np.fabs(update(beta, h))
        #Spins[i] = s
        #Time[i] = i

    sum = 0.0
    for i in range(Measurement): #Dengedeki bölge
        sum += update(beta, h)

    print(beta, sum / Measurement)
    Measurements[b] = sum / Measurement
    Beta[b] = beta
    beta = beta + 0.05
    #plt.plot(Time, Spins)
    #plt.show()
plt.plot(Beta, Measurements)
plt.show()