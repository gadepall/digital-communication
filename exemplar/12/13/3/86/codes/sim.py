import numpy as np

# Set the probability of swimmer(1)
prob_swimmer = 0.7

# Generate 1000 samples of 5 numbers each
num_samples = 1000
num_numbers = 5

# Generate random numbers between 0 and 1 for each sample
samples = np.random.rand(num_samples, num_numbers)

# Convert the random numbers to ones and zeros based on the probability
samples = (samples < prob_swimmer).astype(int)

# Count the number of samples with 4 ones
count = np.sum(samples == 1, axis=1)
four_swimmers = np.sum(count == 4)

prob_fourswimmers = four_swimmers/num_samples
print(f"desired prob = {prob_fourswimmers}")
