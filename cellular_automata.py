import numpy as np
import matplotlib.pyplot as plt

def fire(rule, size, p):

    M = np.zeros((size, size))

    for i in range(size):
        M[0, i] = int(p > np.random.random())

    rule_array = []
    for i in range(8):
        rule_array.append(rule & 1)
        rule >>= 1

    for j in range(size - 1):
        for i in range(1, size - 1):
            r = (int(M[j, i - 1]) << 2) | (int(M[j, i]) << 1) | (int(M[j, i - 1]))
            M[j + 1, i] = rule_array[r]

    plt.imshow(M)
    plt.show()

fire(36, 100, 0.6)
