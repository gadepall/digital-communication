import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 4  
p = 0.10  
k = np.arange(0, n+1)  
binomial_pmf = binom.pmf(k, n, p)
print("Binomial")
print(binomial_pmf[0])
mu = n * p
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(x, mu, sigma)
print("Gaussian")
print(normal_pdf[0])
print("CDF Approximation")
q_value = 1 - norm.cdf(mu/sigma)
print(q_value)
plt.stem(k, binomial_pmf, label='Binomial PMF', basefmt='b-')
plt.plot(x, normal_pdf, label='Normal PDF', color='r')
plt.xlabel('Number of Balls Drawn which are marked zero')
plt.ylabel('Probability / Probability Density')
plt.legend()
plt.title("Binomial PMF vs Gaussian PDF")
plt.savefig("ncert/9/3/10/figs/figure.png")
plt.show()
