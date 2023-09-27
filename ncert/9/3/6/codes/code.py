import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 5   # Number of trials
p = 0.8  # Probability of success


k = np.arange(0, n+1)  # Generate values for x (number of successes in binomial)
binomial_pmf = binom.pmf(k, n, p) # Compute the PMF of the binomial distribution

mu = n * p # Parameters for the normal distribution (approximation to binomial)
sigma = np.sqrt(n * p * (1 - p))
x = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(x, mu, sigma)
plt.stem(k, binomial_pmf, label='Binomial PMF', basefmt='b-') # Plot the binomial PMF
plt.plot(x, normal_pdf, label='Gaussian PDF', color='r') # Plot the normal PDF (approximation)

plt.axvline(x=4, color='g', linestyle='--', label='x=4')
plt.xlabel('Number of Swimmer')
plt.ylabel('Probability')
plt.legend()

plt.savefig("/home/jay/Desktop/ncert1/9.3.6/figs/approx.png")
plt.show()
