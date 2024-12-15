import numpy as np
import matplotlib.pyplot as plt

def reflectanceTE(n1, theta1, n2, theta2): return (n1 * np.cos(theta1) - n2 * np.cos(theta2)) / (n1 * np.cos(theta1) + n2 * np.cos(theta2))
def transmittanceTE(n1, theta1, n2, theta2): return (2 * n1 * np.cos(theta1)) / (n1 * np.cos(theta1) + n2 * np.cos(theta2))
def reflectanceTM(n1, theta1, n2, theta2): return (n2 * np.cos(theta1) - n1 * np.cos(theta2)) / (n2 * np.cos(theta1) + n1 * np.cos(theta2))
def transmittanceTM(n1, theta1, n2, theta2): return (2 * n1 * np.cos(theta1)) / (n2 * np.cos(theta1) + n1 * np.cos(theta2))

def snell(theta_incident, n_curr, n_next): return np.arcsin(n_curr * np.sin(theta_incident) / n_next)

def tranmission_matrix(layer_curr, layer_next, theta_incident, polarization):
    n_curr = layer_curr[0]
    n_next = layer_next[0]
    theta_transmittance = snell(theta_incident, n_curr, n_next)

    if(polarization == "TE"):
        r = reflectanceTE(n_curr, theta_incident, n_next, theta_transmittance)
        t = transmittanceTE(n_curr, theta_incident, n_next, theta_transmittance)
    else:
        r = reflectanceTM(n_curr, theta_incident, n_next, theta_transmittance)
        t = transmittanceTM(n_curr, theta_incident, n_next, theta_transmittance)

    return np.array([[1, r], [r, 1]]) / t, theta_transmittance

def propagation_matrix(λ, L, n, theta_transmittance):
    k = 2 * np.pi * n / λ
    phi = k * L * np.cos(theta_transmittance)
    e = np.exp(phi * 1j)
    return np.array([[e, 0+0j], 
                     [0+0j, 1 / e]])

def ART(layers, theta_incident, λ_set, polarization):
    A = [] 
    R = []
    T = []

    for λ in λ_set:
        M = np.array([[1, 0], [0, 1]]) #unit matrix
        for i in range(len(layers) - 1):
            D, theta_incident = tranmission_matrix(layers[i], layers[i + 1], theta_incident, polarization)
            n_next = layers[i + 1][0]
            L_next = layers[i + 1][1]
            P = propagation_matrix(λ, L_next, n_next, theta_incident)
            M = np.matmul(M, np.matmul(D, P))
    
        R_λ = np.absolute(M[1][0] / M[0][0])**2
        T_λ = np.absolute(1 / M[0][0])**2
        A_λ = 1 - R_λ - T_λ
        A.append(A_λ)
        R.append(R_λ)
        T.append(T_λ)

    return A, R, T


"""
layer = [refractive index, thickness]
"""

layers = [[1, 0], #air
          [3.9595, 1 * 1e-6],
          [1, 0]] #air

theta_incident = 0

domain = "λ"
if(domain == "F"):
    F = np.linspace(1e13, 1e15, 1000)
    A, R, T = ART(layers, theta_incident, 3e8 / F, "TE")
    x = F
else:
    λ = np.linspace(1, 15, 1000) * 1e-6
    A, R, T = ART(layers, theta_incident, λ, "TE")
    x = λ

plt.subplot(3,1,1)
plt.plot(x, T)
plt.legend("T")
plt.subplot(3,1,2)
plt.plot(x, R)
plt.legend("R")
plt.subplot(3,1,3)
plt.plot(x, A)
plt.legend("A")
plt.show()
