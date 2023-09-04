import numpy as np

# Set the probabilities
prob_red = 1/2
prob_king = 1/13

# Number of cards
num_cards = 52

# Generate the entries
value_red = np.random.choice([0, 1], size=num_cards, p=[1 - prob_red, prob_red])
value_king = np.random.choice([0, 1], size=num_cards, p=[1 - prob_king, prob_king])

cards = np.block([value_red[:, np.newaxis], value_king[:, np.newaxis]])

# Count the number of cards with both elements as zeroes
zero_zero_count = np.count_nonzero((cards == [0, 0]).all(axis=1))

desired_prob=(num_cards-zero_zero_count)/num_cards

print(f"probabaility:{desired_prob}")
print(f"simulation:{cards}")

