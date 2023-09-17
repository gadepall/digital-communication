import numpy as np

values = np.array([2, 3, 4])
probabilities = np.array([0.2, 0.5, 0.3])

# Calculate the mean of X
mean = np.sum(values * probabilities)

# Calculate the variance of X
variance = np.sum((values - mean)**2 * probabilities)

# Calculate the standard deviation of X
std_deviation = np.sqrt(variance)

# Print the results
print(f"Mean (Expected Value): {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

