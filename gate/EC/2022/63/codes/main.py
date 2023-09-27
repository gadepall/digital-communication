import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

p = 0.1
n = 7
q = 1 - p

y_values = np.arange(0, n + 1, 1)

# Calculate the binomial PMF (probability mass function) for Y
binomial_pmf = binom.pmf(y_values, n, p)

# Calculate the CDF for the binomial distribution
binomial_cdf = np.cumsum(binomial_pmf)

print(f"the probability that a transmitted codeword is decoded correctly is {binomial_cdf[1]}")

# Calculate the mean and standard deviation of the binomial distribution
mean = n * p
variance = n * p * q

# Calculate the CDF for a Gaussian distribution using the mean and standard deviation of the binomial
normal_cdf = norm.cdf(y_values + 0.33, loc=mean, scale=np.sqrt(variance))

print(f"the probability that a transmitted codeword is decoded correctly is {normal_cdf[1]}")

# Plot the results
plt.figure(figsize=(10, 6))
plt.stem(y_values, binomial_cdf, label="Binomial CDF")
plt.plot(y_values, normal_cdf, label="Gaussian CDF", linestyle='dashed')
plt.xlabel("Y")
plt.ylabel("CDF")
plt.legend()
plt.title("Binomial CDF vs. Gaussian CDF")
plt.grid(True)
plt.savefig('/home/karthikeya/Desktop/Probability/New_assignment8/figs/figure1.png')
plt.show()

