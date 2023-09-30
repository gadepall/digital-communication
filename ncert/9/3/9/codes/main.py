from scipy.stats import norm
from scipy.stats import binom
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mping

p = 0.05
n = 5
k = 0
sig = np.sqrt(n*p*(1-p))
print("For k = 0")
print("Probability from Gaussian approximation: ",norm.cdf((k-n*p+0.5)/sig))
print("Probability from Binomial: ",(binom.cdf(k,n,p)))
k = 1
print("For k = 1")
print("Probability from Gaussian approximation: ",norm.cdf((k-n*p+0.5)/sig))
print("Probability from Binomial: ",(binom.cdf(k,n,p)))


sig = np.sqrt(n*p*(1-p))
k = np.linspace(0,n,n+1)
fig, ax = plt.subplots()
#binomial
xpoints = k
ypoints = np.array(binom.pmf(k,n,p))
ax.stem(xpoints, ypoints,linefmt='r-', markerfmt='ro', basefmt='k--')
#gauss
xpoints = np.arange(-2,n,0.01)
ypoints = np.array(norm(n*p,sig).pdf(xpoints))
#ypoints = norm.pdf(xpoints,(n*p),sig)
ax.plot(xpoints, ypoints,'b')
plt.legend(["Binomial","Gaussian"])
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.grid()
plt.savefig("bg.png")
