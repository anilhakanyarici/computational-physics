import numpy as np
import matplotlib.pyplot as plt

NX = 10
NY = 10
NPatterns = 1
Volume = NX * NY
S = np.zeros(Volume, dtype = int)
W = np.zeros((Volume, Volume), dtype = float)
N = np.zeros((NPatterns, Volume), dtype = int)

def fill_picture():
	for ip in range(NPatterns):
		for i in range(Volume):
			N[ip, i] = 2 * np.random.randint(2) - 1

def fill_weights():
	global W
	for i in range(Volume):
		for j in range(Volume):
			W[i, j] = 0 #sürekli sabit gelecek. -1 iken full 0 gelecek
			for ip in range(NPatterns):
				W[i, j] = W[i, j] + N[ip, i] * N[ip, j]
	W[i, i] = 0

def fill_neurons(ip, prb):
	global S
	for i in range(Volume):
		#S[i] = np.random.randint(2) - 1
		S[:] = N[ip,:]
	for i in range(Volume):
		if(prb > np.random.random()): S[i] = -S[i]

def update(beta):
	global S
	for i in range(Volume):
		sum = 0
		for j in range(Volume):
			sum = sum + W[i, j] * S[j]
		
		#1. yöntem
		deltaE = -2 * S[i] * sum
		if deltaE > np.random.random(): S[i] = -S[i]
		
		#2. yöntem
		'''
		S[i] = -1
		if(0.5 * (1 + np.tanh(sum * beta / Volume)) > np.random.random()):
			S[i] = 1
		'''
fill_picture()
fill_neurons(0, 0.1)
fill_weights()
SUM = np.zeros(NPatterns)
for it in range(10):
	update(1.1)
	for ip in range(NPatterns):
		sum = 0
		for i in range(Volume):
			sum  = sum + N[ip, i] * S[i]
		SUM[ip] = sum
	'''
	sum = 0
	for j in range(Volume):
		sum = sum + S[j]
	print("%4d %6.3f"%(it, np.abs(sum / float(Volume))))
	'''
print(SUM)

plt.imshow(S.reshape(NY, NX))
plt.imshow(N[0].reshape(NY, NX))
plt.show()