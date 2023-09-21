import numpy as np

# Number of simulations and defining the values on cards
num_simulations = 100000
cards = np.arange(1, 6)

# Simulate the scenario and calculate X for each simulation
selected_indices = np.random.choice(len(cards), size=(num_simulations, 2))
selected_cards = cards[selected_indices]

# Filter out cases where both cards have the same value
selected_cards = selected_cards[selected_cards[:, 0] != selected_cards[:, 1]]

X_simulated = np.sum(selected_cards, axis=1)

# Calculate the simulated mean and variance
simulated_mean = np.mean(X_simulated)
simulated_variance = np.var(X_simulated)

# Create all possible combinations of two cards without replacement
combinations = np.array(np.meshgrid(cards, cards)).T.reshape(-1, 2)
combinations = combinations[combinations[:, 0] != combinations[:, 1]]

# Calculate the PMF using NumPy (Vectorized)
X_values = np.arange(3, 10)
count = np.sum(combinations[:, 0] + combinations[:, 1] == X_values[:, np.newaxis], axis=1)
p_X_theoretical = count / len(combinations)

# Calculate theoretical mean and variance (Vectorized)
theoretical_mean = np.dot(X_values, p_X_theoretical)
theoretical_variance = np.dot(X_values**2, p_X_theoretical) - theoretical_mean**2

print("Theoretical Mean:", theoretical_mean)
print("Simulated Mean:", simulated_mean)
print("Theoretical Variance:", theoretical_variance)
print("Simulated Variance:", simulated_variance)

