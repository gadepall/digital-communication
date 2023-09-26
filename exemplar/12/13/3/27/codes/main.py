import numpy as np

# Number of pairs to generate
num_pairs = 10000

# Probability of getting 1 in each pair
probability_of_one = 0.1

# Generate the pairs using NumPy
pairs = np.random.choice([0, 1], size=(num_pairs, 2), p=[1 - probability_of_one, probability_of_one])

# Calculate the count of 1s in each pair
count_of_ones = np.sum(pairs, axis=1)

variance = np.var(count_of_ones)

print(variance)

