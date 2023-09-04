from scipy.stats import norm
from scipy.stats import binom
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

n = 20  
p = 0.5
sig = np.sqrt(n*p*(1-p))
k = np.linspace(0,n,n+1)
fig, ax = plt.subplots()
xpoints = k
ypoints = np.array(binom.pmf(k,n,p))
ax.stem(xpoints, ypoints,linefmt='r-', markerfmt='ro', basefmt='k--')
xpoints = np.linspace(0,n,100*n)
ypoints = np.array(norm(n*p,sig).pdf(xpoints))
ax.plot(xpoints, ypoints,'b')
plt.xlim(n*p-2*sig,n*p+2*sig)
plt.legend(["Gaussian","Binomial"])
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
str = str(n) +".eps"
plt.savefig(str, format='eps')
plt.close(fig)
