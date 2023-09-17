import numpy as np

# Number of simulations
num_simulations = 100000

# Create a deck of cards with 4 aces and 48 non-aces (total 52 cards)
deck = np.array(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4)

# Simulate drawing two cards without replacement for all simulations
drawn_cards = np.random.choice(deck, size=(num_simulations, 2), replace=False)

# Count the number of aces in each pair of drawn cards
ace_counts = np.sum(drawn_cards == 'A', axis=1)

# Calculate the simulated mean and standard deviation
simulated_mean = np.mean(ace_counts)
simulated_std_dev = np.std(ace_counts)

# Theoretical mean and standard deviation (calculated previously)
theoretical_mean = 0.1538
theoretical_std_dev = 0.373

# Print the results
print("Simulated Mean:", simulated_mean)
print("Theoretical Mean:", theoretical_mean)
print("Simulated Standard Deviation:", simulated_std_dev)
print("Theoretical Standard Deviation:", theoretical_std_dev)

