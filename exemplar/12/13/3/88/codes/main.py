import numpy as np
import random

#Simulation
X = [-4]*1 + [-3]*2 + [-2]*3 + [-1]*2 + [0]*2
random.shuffle(X)

simlen = 10000
choice_X = np.random.choice(X, size = simlen)
E_X = sum(choice_X)/simlen

print("Expectation through Simulation:")
print(E_X)

#Theoretical
X_th = np.array([-4,-3,-2,-1,0])
P_X = np.array([0.1,0.2,0.3,0.2,0.2])

E_X = sum(X_th*P_X)
print("Theoretical Expectation")
print(E_X)

