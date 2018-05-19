import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

y1 = 3
y2 = 1
y3 = 2

t_start = 0
t_end = 60
t_step = 0.001

def DY1(y1, y2, y3):
    return sigma * (y2 - y1)
def DY2(y1, y2, y3):
    return y1 * (rho - y3) - y2
def DY3(y1, y2, y3):
    return y1 * y2 - beta * y3

Y1 = []
Y2 = []
Y3 = []
Y1.append(y1)
Y2.append(y2)
Y3.append(y3)
t_current = t_start
while(t_current < t_end):
    k1 = t_step * DY1(y1, y2, y3)
    l1 = t_step * DY2(y1, y2, y3)
    m1 = t_step * DY3(y1, y2, y3)

    k2 = DY1(y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
    l2 = DY2(y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
    m2 = DY3(y1 + k1 / 2, y2 + l1 / 2, y3 + m1 / 2)
    
    y1 = y1 + t_step * k2
    y2 = y2 + t_step * l2
    y3 = y3 + t_step * m2

    Y1.append(y1)
    Y2.append(y2)
    Y3.append(y3)

    t_current += t_step

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(Y1, Y2, Y3)
plt.show()