import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 5  # Number of trials
p = 0.25  # Probability of success

# Parameters for the normal distribution (approximation to binomial)
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Generate values for x (number of successes in binomial)
x = np.arange(0, n+1)

# Compute the PMF of the binomial distribution
binomial_pmf = binom.pmf(x, n, p)

# Generate values for y (PDF of the normal distribution)
y = np.linspace(0, n, 1000)
normal_pdf = norm.pdf(y, loc=mu, scale=sigma)

# Plot the binomial PMF
plt.stem(x, binomial_pmf, basefmt=" ", markerfmt="bo", linefmt="b-", label='Binomial PMF')

# Plot the normal PDF (approximation)
plt.plot(y, normal_pdf, label='Normal PDF', color='red')

# Add labels and legend
plt.xlabel('Number of Successes')
plt.ylabel('Probability / Probability Density')
plt.legend()

# Show the plot
plt.title('Binomial PMF vs. Normal PDF')
plt.grid(True)
plt.savefig("../figs/plot.pdf")

