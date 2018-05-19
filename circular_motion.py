import math
import matplotlib.pyplot as plt

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

def U(r_mag):
     alpha = 0.8
     return alpha / r_mag

def F(r):
    dr = 0.01
    n = r.unit() * -1
    return n * -(U(r.magnitude() + dr) - U(r.magnitude() - dr)) / (2 * dr)

r = Vector(1, 0)
v = Vector(0, 1)

t_start = 0
t_end = 30
t_step = 0.01

X = []
Y = []
V = []

X.append(r.x)
Y.append(r.y)

t_current = t_start
while(t_current < t_end):
    k1 = F(r) * t_step
    l1 = v * t_step

    k2 = F(r + k1 / 2)
    l2 = v + l1 / 2

    v = v + k2 * t_step
    r = r + l2 * t_step

    X.append(r.x)
    Y.append(r.y)

    t_current += t_step

plt.plot(X, Y)
plt.show()
