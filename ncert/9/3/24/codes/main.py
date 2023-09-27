import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm
n = 10
p = 0.5
k = 8
mean = n * p
stddev = np.sqrt(n * p * (1 - p))
probability_at_least_k_gaussian = 1 - norm.cdf(k - 0.5, loc=mean, scale=stddev)
x_gaussian = np.arange(0, n + 1, 0.01)
pmf_binomial = binom.pmf(np.arange(0, n + 1), n, p)
probability_at_least_k_binomial = sum(pmf_binomial[k:])
plt.plot(x_gaussian, norm.pdf(x_gaussian, loc=mean, scale=stddev), color='red', label='Gaussian Distribution')
plt.stem(np.arange(0, n + 1), pmf_binomial, linefmt='b-', markerfmt='bo', basefmt=' ', label='Binomial Distribution (Stem)')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Probability Distribution of Getting at Least 8 Heads in 10 Coin Tosses')
plt.legend()
plt.grid(True)
plt.savefig('Figuregvb.png')
plt.show()

