import numpy as np

# Number of simulations
num_simulations = 100000

# Simulate the genders of all children at once
families = np.random.randint(2, size=(num_simulations, 3))

# Count the number of girls in each family
num_girls = np.sum(families, axis=1)

# Calculate the probabilities
probability_no_girls = np.mean(num_girls == 0)
probability_one_girl = np.mean(num_girls == 1)
probability_two_girls = np.mean(num_girls == 2)
probability_three_girls = np.mean(num_girls == 3)

# Print the results
print("Probability of No Girls:", probability_no_girls)
print("Probability of One Girl:", probability_one_girl)
print("Probability of Two Girls:", probability_two_girls)
print("Probability of Three Girls:", probability_three_girls)
