import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.stats import norm 

p = 0.5
n = 8
k = 3
mean = n*p
var = n*p*(1-p)

def norm_pdf(x):
    return 1/math.sqrt(2*math.pi)*pow(math.e,-x*x/var)

print("Bernoulli probability: ", binom.pmf(k,n,p))
print("Guassian probability: ", norm.pdf((k-mean)/var) )

x = np.arange(0, n+1)
binomial_pmf = binom.pmf(x, n, p)

y = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(y-mean)

plt.stem(x, binomial_pmf, basefmt=" ", markerfmt="ro", linefmt="red", label='Binomial PMF')
plt.plot(y, normal_pdf, color='darkblue', label='Normal PDF')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.legend()
plt.grid()
plt.savefig("../figs/fig.png")
