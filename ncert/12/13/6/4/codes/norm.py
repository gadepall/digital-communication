from scipy.stats import norm
from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

p = 0.5
n = 20
k = 8
sig = np.sqrt(n*p*(1-p))

xpoints = np.linspace(0,n,n+1)
ypoints = np.array(binom.cdf(xpoints,n,p) )
plt.stem(xpoints, ypoints,linefmt='r-', markerfmt='ro', basefmt='k--')
xpoints = np.linspace(0,n,100*n)
ypoints = np.array(norm.cdf((xpoints-n*p+0.5)/sig))
plt.plot(xpoints, ypoints,'b')
print(norm.cdf((k-n*p+0.5)/sig))
print((binom.cdf(k,n,p)))
plt.show() 
