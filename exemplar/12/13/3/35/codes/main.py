import numpy as np
num_simulations = 100000
dice_rolls = np.random.randint(1, 7, size=(num_simulations, 2))
max_values = np.max(dice_rolls, axis=1)
unique_values, counts = np.unique(max_values, return_counts=True)
probabilities = counts / num_simulations
print("Maximum values:", unique_values)
print("Probabilities:", probabilities)
mean = np.sum(unique_values * probabilities)
print(f"Mean of the distribution: {mean}")

