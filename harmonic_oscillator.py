import matplotlib.pyplot as plt

k1 = 1
k = 1
k2 = 1
M1 = 1
M2 = 1
x1 = -1
x2 = 1
v1 = 0
v2 = 0

t_start = 0
t_end = 25
t_step = 0.01


def DX1(x1, x2, v1, v2):
    return v1

def DX2(x1, x2, v1, v2):
    return v2

def DV1(x1, x2, v1, v2):
    return (k * (x2 - x1) - k1 * x1) / M1

def DV2(x1, x2, v1, v2):
    return (k * (x1 - x2) - k2 * x2) / M2

X1 = []
X2 = []
T = []

X1.append(x1)
X2.append(x2)
T.append(t_start)

t_current = t_start
while(t_current < t_end):
    k1 = t_step * DX1(x1, x2, v1, v2)
    l1 = t_step * DX2(x1, x2, v1, v2)
    m1 = t_step * DV1(x1, x2, v1, v2)
    n1 = t_step * DV2(x1, x2, v1, v2)

    k2 = DX1(x1 + k1 / 2, x2 + l1 / 2, v1 + m1 / 2, v2 + n1 / 2)
    l2 = DX2(x1 + k1 / 2, x2 + l1 / 2, v1 + m1 / 2, v2 + n1 / 2)
    m2 = DV1(x1 + k1 / 2, x2 + l1 / 2, v1 + m1 / 2, v2 + n1 / 2)
    n2 = DV2(x1 + k1 / 2, x2 + l1 / 2, v1 + m1 / 2, v2 + n1 / 2)

    x1 = x1 + t_step * k2
    x2 = x2 + t_step * l2
    v1 = v1 + t_step * m2
    v2 = v2 + t_step * n2

    X1.append(x1)
    X2.append(x2)

    t_current += t_step
    T.append(t_current)

plt.plot(T, X1)
plt.plot(T, X2)
plt.show()
