#6.1.5 PDF
import numpy as np
import mpmath as mp
import scipy 
from scipy.stats import rayleigh
import matplotlib.pyplot as plt
from math import exp
from math import sqrt
#if using termux
import subprocess
import shlex
#end if


N = np.arange(-10,-0.00001,0.1)#points on the x axis

def Pe(x):
    return 1-exp((-x**2)/2)

vect_Pe = scipy.vectorize(Pe)

#simulation
simlen = int(1e3)

prob = []
lis=[]
for i in range(0, 100):
    prob_sum = 0
    for j in range(simlen):
        prob_sum += ss.rayleigh.cdf(-N[i], loc = 0, scale = 1)
        lis.append(ss.rayleigh.cdf(-N[i], loc = 0, scale = 1))
    prob_sum /= simlen
    prob.append(prob_sum)

plt.plot(N, vect_Pe(N), '-')
plt.plot(N, prob, 'o')
plt.xlabel('$N$')
plt.ylabel('$P_e(N)$')
plt.legend(["Theoretical", "Simulated"])
plt.grid()