import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Vector:
    x = 0
    y = 0
    z = 0
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)


    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, s): #skaler sayı ile çarpma
        return Vector(self.x * s, self.y * s, self.z * s)

    def __truediv__(self, s): #skaler sayıya bölme
        return Vector(self.x / s, self.y / s,self.z / s)

    def unit(self):
        m = self.magnitude()
        return Vector(self.x / m, self.y / m, self.z / m)

q = 1
m = 1
E = Vector(0, 10, 0)
B = Vector(0, 10, 0)
r = Vector(0, 0, 0)
v = Vector(10, 10, 0)

t_start = 0
t_end = 30
t_step = 0.01

def DR(r, v):
    return v

def DV(r, v):
    VxB_x = v.y * B.z - v.z * B.y
    VxB_y = v.z * B.x - v.x * B.z
    VxB_z = v.x * B.y - v.y * B.x
    VxB = Vector(VxB_x, VxB_y, VxB_z)
    return (E + VxB) * q / m

X = []
Y = []
Z = []
X.append(r.x)
Y.append(r.y)
Z.append(r.z)

t_current = t_start
while(t_current < t_end):
    k1 = DV(r, v) * t_step
    l1 = DR(r, v) * t_step

    k2 = DV(r + l1 / 2, v + k1 / 2)
    l2 = DR(r + l1 / 2, v + k1 / 2)

    r = r + l2 * t_step
    v = v + k2 * t_step

    X.append(r.x)
    Y.append(r.y)
    Z.append(r.z)

    t_current += t_step

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z)
plt.show()
