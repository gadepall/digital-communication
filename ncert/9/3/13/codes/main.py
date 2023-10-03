import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 7 
p =   1/6
k = np.arange(0, n+1)  
binomial_pmf = binom.pmf(k, n, p)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(x, mu, sigma)
plt.stem(k, binomial_pmf, label='Binomial PMF', basefmt='b-')
plt.plot(x, normal_pdf, label='Normal PDF', color='r')
plt.axvline(x=2, color='y', linestyle='dotted', label='x=2')
plt.xlabel('Number of 5 appearing on dice')
plt.ylabel('Probability')
plt.legend()
plt.savefig("../figs/figure.png")
plt.show()
