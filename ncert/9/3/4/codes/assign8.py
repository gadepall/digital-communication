import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

n = 20
p = 0.5
# Number of correct answers to consider
k = 12
# Mean and standard deviation of the Gaussian distribution
mean = n * p
stddev = np.sqrt(n * p * (1 - p))
# Calculate the probability of answering at least k questions correctly using Gaussian
probability_at_least_k_gaussian = 1 - norm.cdf(k - 0.5, loc=mean, scale=stddev)
# Create a range of values for the x-axis (number of correct answers)
x = np.arange(0, n+1)
# Calculate the corresponding binomial probability mass function values
pmf_binomial = binom.pmf(x, n, p)
# Calculate the probability of answering at least k questions correctly using binomial
probability_at_least_k_binomial = 1 - sum(pmf_binomial[:k])

# Plot the Gaussian distribution as a curve
plt.plot(x, norm.pdf(x, loc=mean, scale=stddev), color='red', label='Gaussian Distribution')
# Use a stem plot for the binomial distribution
plt.stem(x, pmf_binomial, linefmt='b-', markerfmt='bo', basefmt=' ', label='Binomial Distribution (Stem)')
plt.xlabel('Number of Correct Answers')
plt.ylabel('Probability')
plt.title('Probability Distribution of Correct Answers')
plt.legend()
plt.grid(True)
# Save the figure as a PNG file
plt.savefig('distributions.png')
# Display the calculated probabilities for at least k correct answers
print(f"Probability of answering at least {k} questions correctly (Gaussian): {probability_at_least_k_gaussian}")
print(f"Probability of answering at least {k} questions correctly (Binomial): {probability_at_least_k_binomial}")

plt.show()

