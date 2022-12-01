#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss
#if using termux
import subprocess
import shlex
#end if


gamma_dB = np.linspace(0, 10, 11)

def Pe(x):
    return 0.5 - 0.5*(math.sqrt(x/(2+x)))

vect_Pe = []

#simulation
simlen = int(1e5)
N = np.random.normal(0,1,simlen)

prob = []

for i in range(0, 11):

  gamma = 10**(0.1*gamma_dB[i])
  
  A=ss.rayleigh.rvs( loc = 0, scale = math.sqrt((gamma)/2),size=simlen)
  prob_sum = 0
  for j in range(simlen):
    if A[j]+N[j]<0:
      prob_sum=prob_sum+1
        
  prob_sum /= simlen
  prob.append(prob_sum)
  vect_Pe.append(Pe(gamma))


plt.semilogy(gamma_dB.T, vect_Pe, '-')
plt.semilogy(gamma_dB.T, prob, 'o')
plt.xlabel('$\gamma$ in dB')
plt.ylabel('$P_e(\gamma)$')
plt.legend(["Theoretical", "Simulated"])
plt.grid()
#if using termux
#plt.savefig('figs/cond/Pe_vs_gamma.pdf')
#plt.savefig('figs/cond/Pe_vs_gamma.eps')
#subprocess.run(shlex.split("termux-open figs/cond/Pe_vs_gamma.pdf"))
#else
plt.show() #opening the plot window