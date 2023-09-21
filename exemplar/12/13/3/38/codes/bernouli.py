import numpy as np

# Define the possible outcomes for a single die roll
die_outcomes = np.array([1, 2, 3, 4, 5, 6])

# Calculate the probability distribution for a single die roll
die_probabilities = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# Use broadcasting to calculate the joint probabilities for two dice rolls
joint_probabilities = np.outer(die_probabilities, die_probabilities)

# Calculate the probability of the sum of two dice rolls being 6
sum_6_probability = np.sum(joint_probabilities[np.where(6 == np.add.outer(die_outcomes, die_outcomes))])

# Calculate the probability of the sum of two dice rolls being 7
sum_7_probability = np.sum(joint_probabilities[np.where(7 == np.add.outer(die_outcomes, die_outcomes))])

probablity = (1-sum_6_probability)*(1-sum_7_probability)*(sum_6_probability)
print(probablity)
