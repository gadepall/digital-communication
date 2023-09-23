import numpy as np

# Define the deck of cards
deck = np.array(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4)

# Define the number of simulations
num_simulations = 1000000  # You can adjust this number as needed

# Simulate drawing two cards with replacement and check if both are queens
simulations = np.random.choice(deck, size=(num_simulations, 2), replace=True)
both_queens = np.all(simulations == 'Q', axis=1)

# Calculate the probability of both cards being queens
probability = np.sum(both_queens) / num_simulations

print(f"Simulated Probability: {probability}")

