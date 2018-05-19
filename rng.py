#numerical recipes
#abramovitz

#importance sampling

import random
import matplotlib.pyplot as plt

count = 1000
R = []
sum = 0
for i in range(count):
    r = random.random()
    R.append(r)
    sum += r
sum /= count
print(sum)

#plt.plot(R[0::2], R[1::2])
plt.hist(R)
plt.show()
