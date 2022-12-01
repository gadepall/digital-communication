import numpy as np
# import uniform distribution
from scipy.stats import uniform
from matplotlib import pyplot as plt

#if using termux
import subprocess
import shlex
#end if


def ecdf(a):
    x, counts = np.unique(a, return_counts=True)
    cusum = np.cumsum(counts)
    return x, cusum / cusum[-1]

U = uniform.rvs(size=1000)
V=-2*np.log(1-U)
x, y = ecdf(V)
x = np.insert(x, 0, x[0])
y = np.insert(y, 0, 0.)
plt.plot(x, y,'o',label='Simulation')
plt.grid(True)
v=np.linspace(0,15,100)
plt.plot(v,1-np.exp(-v/2),label='Analysis')
plt.title("CDF of random variable $V$")
plt.xlabel("$v$")
plt.ylabel("$F_V(v)$")
plt.legend(loc='best')
#if using termux
plt.savefig('./figs/quantile.pdf')
plt.savefig('./figs/quantile.png')
subprocess.run(shlex.split("termux-open ./figs/quantile.pdf"))
#else
#plt.show()





