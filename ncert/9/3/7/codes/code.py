import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 10  # Number of trials
p = 0.05  # Probability of success (defective item)
k = np.arange(0, n + 1)  # Possible number of defective items
binomial_pmf = binom.pmf(k, n, p)

mu = n * p  # Mean of the Gaussian distribution
sigma = np.sqrt(n * p * (1 - p))  # Standard deviation of the Gaussian distribution
x = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(x, mu, sigma)

plt.stem(k, binomial_pmf, label='Binomial PMF', basefmt='b-')
plt.plot(x, normal_pdf, label='Gaussian PDF', color='r')
plt.xlabel('Number of Defective Items')
plt.ylabel('Probability/Density')
plt.legend()
plt.grid(True)
plt.savefig('../figs/fig.png')
#plt.show()

