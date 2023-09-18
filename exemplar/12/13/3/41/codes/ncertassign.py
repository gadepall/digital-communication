import numpy as np

# Define the probabilities of choosing each bag
bag_probabilities = np.array([1/6, 2/6, 3/6])  # i/6, i=1,2,3

# Define the probabilities of selecting a red or white ball from each bag
bag_contents = np.array([[3, 0], [2, 1], [0, 3]])  # [red, white]

# Calculate the probability of selecting a red ball
red_prob = np.sum(bag_probabilities * (bag_contents[:, 0] / 3))

# Calculate the probability of selecting a white ball
white_prob = np.sum(bag_probabilities * (bag_contents[:, 1] / 3))

print("Probability of selecting a red ball:", red_prob)
print("Probability of selecting a white ball:", white_prob)

