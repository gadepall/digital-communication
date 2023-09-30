import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import math

# Parameters
n = 5  # Total number of persons
p_not_swimmer = 0.3  # Probability that a person is not a swimmer
p_swimmer = 1 - p_not_swimmer  # Probability that a person is a swimmer
k = 4  # Number of swimmers we want

# Calculate the expected value (mean) and standard deviation
mu = n * p_swimmer
sigma = np.sqrt(n * p_swimmer * (1 - p_swimmer))

# Create an array of x values for the PDF graph
x = np.linspace(0, n, 1000)

# Calculate the PDF values for the x values
pdf_values = stats.norm.pdf(x, loc=mu, scale=sigma)

# Calculate probabilities for all possible values of k
k_values = list(range(n + 1))
probabilities = [math.comb(n, k) * (p_swimmer ** k) * (p_not_swimmer ** (n - k)) for k in k_values]

# Plot both figures on the same graph
plt.figure(figsize=(12, 6))

# Plot the Gaussian approximation
plt.plot(x, pdf_values, label='Gaussian Approximation (PDF)')
plt.fill_between(x, 0, pdf_values, where=(x >= k - 0.5) & (x <= k + 0.5), alpha=0.3, label='Probability (Gaussian)')

# Plot the stem plot for the PMF
plt.stem(k_values, probabilities, basefmt=' ', linefmt='r-', markerfmt='ro', label='Probability (PMF)')

plt.xlabel('Number of Swimmers (k)')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)

plt.show()

