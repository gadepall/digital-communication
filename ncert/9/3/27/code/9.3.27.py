import numpy as np
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 7  # Number of trials
p = 0.25  # Probability of success in a single trial

# Calculate the mean (mu) and standard deviation (sigma) for the Gaussian approximation
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Define the range of successful outcomes (hits)
hits_range = np.arange(2, n + 1)

# Calculate the probabilities for hitting the target at least twice with continuity correction using Gaussian approximation
probabilities_gaussian = []

for k in hits_range:
    # Apply continuity correction
    lower_bound = k - 0.5
    upper_bound = k + 0.5

    # Calculate the cumulative probabilities using the Gaussian approximation
    lower_cdf = norm.cdf(lower_bound, loc=mu, scale=sigma)
    upper_cdf = norm.cdf(upper_bound, loc=mu, scale=sigma)

    # Calculate the probability for the range [lower_bound, upper_bound] and append to the list
    probability = upper_cdf - lower_cdf
    probabilities_gaussian.append(probability)

# Calculate the total probability of hitting the target at least twice using Gaussian approximation
total_probability_gaussian = sum(probabilities_gaussian)

# Calculate the probabilities for hitting the target at least twice using the binomial distribution
probabilities_binomial = []

probability_at_least_two = 1 - binom.cdf(1, n, p)

# Print the result

# Print the total probability of hitting the target at least twice using both methods
print("\nTotal Probability of hitting the target at least twice:")
print(f"Gaussian Approximation: {total_probability_gaussian:.6f}")
print(f"Probability of hitting the target at least twice using binomial distribution: {probability_at_least_two:.6f}")

